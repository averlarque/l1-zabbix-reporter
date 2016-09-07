from zabbix import ZabbixApi
import sqlite3
import webbrowser
import os
from handlers import p_load
from pathlib import PurePath
from app import render


class CountPeriodReport:
	"""Parent class for different report"""
	def __init__(self, since, till):
		self.creds = p_load()
		self.zabbix = ZabbixApi(self.creds['host'], self.creds['user'],
		                        os.environ.get('pass'))
		self.since = since
		self.till = till
		self.db = ':memory:'
		self.tables = {'events': 'Events', 'alerts': 'Alerts'}
		self.general_report_data = self.get_general_report_data()

	def get_general_report_data(self):
		result = ['Period: ' + str(self.since) + ' - ' + str(self.till) + '\n',
			     'Monitoring system: Zabbix \n']
		return result

	@staticmethod
	def _generator(items):
		for i in items:
			yield i

	def create_db_tables(self):
		query = '''

		CREATE TABLE IF NOT EXISTS {0} (
			trigger_id INTEGER UNIQUE PRIMARY KEY,
			alert_name TEXT UNIQUE
			);

		CREATE TABLE IF NOT EXISTS {1} (
			trigger_id INTEGER,
			event_id TEXT UNIQUE,
			event_time TEXT,
			event_value TEXT
			);'''.format(self.tables['alerts'], self.tables['events'])
		return query

	def get_data_from_zabbix_event(self, event):
		if event['value'] == '1':
			event_value = 'PROBLEM'
		elif event['value'] == '0':
			event_value = 'OK'
		else:
			event_value = None
		# Define event time
		event_time = self.zabbix.unix_time_to_datetime(event['clock'])
		# Define trigger id
		trigger_id = int(event['objectid'])
		# Define id of the event
		event_id = event['eventid']
		alert = self.zabbix.get_alert_by_event(event_id)
		for item in self._generator(alert['result']):
			alert_name = item['subject']
			break
		# If iteration pass without break and alert name has not been defined
		else:
			alert_name = 'None'
		# print(alert_name, trigger_id, event_id, event_time, event_value)
		data = {'alert_name': alert_name, 'trigger_id': trigger_id,
		        'event_id': event_id, 'event_time': event_time, 'event_value': event_value}
		return data

	def update_db_tables(self, data):
		query_1 = '''
			INSERT OR IGNORE INTO {} (trigger_id, alert_name) VALUES
					(?, ?);'''.format(self.tables['alerts']), (data['trigger_id'], data['alert_name'])
		query_2 = '''
			INSERT OR IGNORE INTO {} (trigger_id, event_id, event_time, event_value)
					VALUES (?, ?, ?, ?)
			'''.format(self.tables['events']), (data['trigger_id'], data['event_id'],
		                                        data['event_time'], data['event_value'])
		return {'insert_alert': query_1, 'insert_event': query_2}

	def select_query(self):
		query = '''SELECT {0}.alert_name, COUNT({0}.alert_name) AS number_of_alerts
			FROM {0} INNER JOIN {1} ON {0}.trigger_id={1}.trigger_id
			WHERE datetime({1}.event_time)  BETWEEN ? AND ?
			GROUP BY {0}.alert_name;'''.format(self.tables['alerts'], self.tables['events']), (str(self.since), str(self.till))
		return query

	def extract_selected_query_data(self, cursor):
		"""
		Uses select_query() to extract data from the DB
		:param cursor: sqlite object
		:return: list of tuples with data
		"""
		query = self.select_query()
		cursor.execute(query[0], query[1])
		results = cursor.fetchall()
		return results

	def generate_report_data(self):
		# Init connection and DB cursor
		conn = sqlite3.connect(self.db)
		cur = conn.cursor()
		# Create tables if they don't exist
		cur.executescript(self.create_db_tables())
		conn.commit()
		# Return to Zabbix API and insert extracted data to the DB tables
		events = self.zabbix.get_events_by_time(self.since, time_till=self.till)  # List of events
		for event in self._generator(events['result']):
			# Get an event data
			data = self.get_data_from_zabbix_event(event)
			# Update query with extracted event data and execute insertion
			update = self.update_db_tables(data)
			cur.execute(update['insert_alert'][0], update['insert_alert'][1])
			cur.execute(update['insert_event'][0], update['insert_event'][1])
		else:
			conn.commit()

		results = self.extract_selected_query_data(cur)
		conn.close()
		return results

	@staticmethod
	def _check_report_path(file_name, report_type):
		# Check if reports folder exists, if not - create one
		if 'reports' not in os.listdir(os.getcwd()):
			os.mkdir('reports')
		# Check OS to choose type of path used
		p_path = PurePath(os.getcwd()).joinpath('reports').joinpath(file_name + '.' + report_type)
		path = str(p_path)
		return path

	def write_report_data_txt(self, file_object, data):
		"""Writing report data in txt-file"""
		for item in self._generator(data):
			line = item[0] + ' ' + 'x' + str(item[1])
			file_object.writelines(line + '\n')

	def create_txt_report(self, items, file_name):
		"""Generating txt report file"""
		# Check OS to choose type of path used
		path = self._check_report_path(file_name, 'txt')
		# Write into the file
		with open(path, 'w') as f:
			f.writelines(self.general_report_data)
			self.write_report_data_txt(f, items)
		os.startfile(path)

	def write_report_data_html(self, data):
		"""Writing report data in list"""
		lines = [item[0] + ' ' + 'x' + str(item[1]) for item in self._generator(data)]
		return lines

	def create_html_report(self, items, file_name):
		"""Generating html report file"""
		# Check OS to choose type of path used
		path = self._check_report_path(file_name, 'html')
		# Init html page markdown
		report_data = self.write_report_data_html(items)
		if type(report_data) is list:
			typ = '0'
		else:
			typ = '1'
		context = {'general_report_data': self.general_report_data,
		           'file_name': file_name,
		           'report_data': report_data,
		           'type': typ}
			
		# Write into the file
		with open(path, "w+") as f:
			html = render('report_template.tpl', context)
			f.write(html)
		webbrowser.open_new("file:///" + path)


class ProjectCountPeriodReport(CountPeriodReport):
	def __init__(self, since, till, project):
		super().__init__(since, till)
		self.project = project
		self.general_report_data.append('Search project: ' + self.project + '\n')

	def select_query(self):
		query = '''
    		SELECT {0}.alert_name, COUNT({0}.alert_name) AS number_of_alerts
    			FROM {0} INNER JOIN {1} ON {0}.trigger_id={1}.trigger_id
    			WHERE datetime({1}.event_time)  BETWEEN ? AND ?
    			AND {0}.alert_name LIKE '{2}%'
    			GROUP BY {0}.alert_name;
    			'''.format(self.tables['alerts'], self.tables['events'], self.project), (str(self.since),
		                                                                                 str(self.till))
		return query


class ItemCountPeriodReport(CountPeriodReport):
	def __init__(self, since, till, item):
		super().__init__(since, till)
		self.item = item
		self.general_report_data.append('Search item: ' + self.item + '\n')

	def select_query(self):
		query = '''
	        		SELECT {0}.alert_name, COUNT({0}.alert_name) AS number_of_alerts
	        			FROM {0} INNER JOIN {1} ON {0}.trigger_id={1}.trigger_id
	        			WHERE {0}.alert_name LIKE '%{2}%'
	        				AND datetime({1}.event_time)  BETWEEN ? AND ?
	        			GROUP BY {0}.alert_name;
	        			'''.format(self.tables['alerts'], self.tables['events'], self.item), (str(self.since),
																								 str(self.till))
		return query


class EventPeriodReport(CountPeriodReport):

	def select_query(self):
		# Extracting events for required time period
		events_query = '''
    				SELECT trigger_id, event_time FROM {0}
    				WHERE datetime(event_time)  BETWEEN ? AND ?;
    				'''.format(self.tables['events']), (str(self.since), str(self.till))
		# Extracting alerted items for required time period
		triggers_query = '''
    				SELECT {0}.trigger_id, {1}.alert_name FROM {0} INNER JOIN {1}
    				ON {0}.trigger_id={1}.trigger_id
    				WHERE datetime({0}.event_time)  BETWEEN ? AND ? GROUP BY {0}.trigger_id;
    				'''.format(self.tables['events'], self.tables['alerts']), (str(self.since), str(self.till))
		# Dictionary as returning value
		queries = {'events_query': events_query,
				   'triggers_query': triggers_query}
		return queries

	def extract_selected_query_data(self, cursor):
		select_query = self.select_query()
		cursor.execute(select_query['events_query'][0], select_query['events_query'][1])
		events = cursor.fetchall()
		cursor.execute(select_query['triggers_query'][0], select_query['triggers_query'][1])
		triggers = cursor.fetchall()
		# Comparing queries results
		alerts = {}
		for n in triggers:
			alerts[n[1]] = []
			for event in events:
				if n[0] != event[0]:
					continue
				else:
					alerts[n[1]].append(event[1])
		return alerts

	def write_report_data_txt(self, file_object, data):
		for item in self._generator(data):
			file_object.writelines(item + '\n')
			for event in data.get(item):
				file_object.writelines(event + '\n')

	def write_report_data_html(self, data):
		lines = {}
		for item in self._generator(data):
			events =[]
			lines.update(item=events)
			for event in data.get(item):
				events.append(event)
		return lines


class ProjectEventPeriodReport(EventPeriodReport):
	def __init__(self, since, till, project):
		super().__init__(since, till)
		self.project = project
		self.general_report_data.append('Search project: ' + self.project + '\n')

	def select_query(self):
		# Extracting events for required time period
		events_query = '''
	    				SELECT trigger_id, event_time FROM {0}
	    				WHERE datetime(event_time)  BETWEEN ? AND ?;
	    				'''.format(self.tables['events']), (str(self.since), str(self.till))
		# Extracting alerted items for required time period
		triggers_query = '''
	    				SELECT {0}.trigger_id, {1}.alert_name FROM {0} INNER JOIN {1}
	    				ON {0}.trigger_id={1}.trigger_id
	    				WHERE datetime({0}.event_time)  BETWEEN ? AND ?
	    				AND {1}.alert_name LIKE '{2}%' GROUP BY {0}.trigger_id;
	    				'''.format(self.tables['events'], self.tables['alerts'],
								   self.project), (str(self.since), str(self.till))
		# Dictionary as returning value
		queries = {'events_query': events_query,
				   'triggers_query': triggers_query}
		return queries


class ItemEventPeriodReport(EventPeriodReport):
	def __init__(self, since, till, item):
		super().__init__(since, till)
		self.item = item
		self.general_report_data.append('Search item: ' + self.item + '\n')

	def select_query(self):
		# Extracting events for required time period
		events_query = '''
		    				SELECT trigger_id, event_time FROM {0}
		    				WHERE datetime(event_time)  BETWEEN ? AND ?;
		    				'''.format(self.tables['events']), (str(self.since), str(self.till))
		# Extracting alerted items for required time period
		triggers_query = '''
		    				SELECT {0}.trigger_id, {1}.alert_name FROM {0} INNER JOIN {1}
		    				ON {0}.trigger_id={1}.trigger_id
		    				WHERE datetime({0}.event_time)  BETWEEN ? AND ?
		    				AND {1}.alert_name LIKE '%{2}%' GROUP BY {0}.trigger_id;
		    				'''.format(self.tables['events'], self.tables['alerts'],
									   self.item), (str(self.since), str(self.till))
		# Dictionary as returning value
		queries = {'events_query': events_query,
				   'triggers_query': triggers_query}
		return queries
