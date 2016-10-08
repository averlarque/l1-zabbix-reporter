from report_generator import *
from datetime import datetime
from report_templates import PeriodReport, ProjectPeriodReport, ItemPeriodReport


# Temporary vars
START_TIME = datetime(2016, 7, 27, 21, 00)
END_TIME = datetime(2016, 7, 28, 4, 00)


def test_parent_update_query():
	report = CountPeriodReport(START_TIME, END_TIME)
	data = {'alert_name': 'PM: Elysium: Error rate > 0.1%: PROBLEM (pm)',
	        'trigger_id': '29934', 'event_id': '27651461',
	        'event_time': '2016-05-28 20:31:57', 'event_value': 'PROBLEM'}
	query = report.update_db_tables(data)

	print('Check for length of the result - 2')
	if len(query) == 2: print(True)
	else: print(False)
	print('Check for type of result - tuple')
	if type(query['insert_alert']) is tuple and type(query['insert_event']) is tuple:
		print(True)
	else: print(False)
	print('Check for types of the result items - str and tuple')
	if type(query['insert_alert'][0]) is str and type(query['insert_event'][1]) is tuple:
		print(True)
	else: print(False)


def test_parent_select_query():
	report = CountPeriodReport(START_TIME, END_TIME)
	query = report.select_query()
	print('Check for length of a returned result - 2')
	if len(query) == 2: print(True)
	else: print(False)
	print('Check for type of the result - tuple')
	if type(query) is tuple: print(True)
	else: print(False)
	print('Check for type of the result items - str and tuple')
	if type(query[0]) is str and type(query[1]) is tuple: print(True)
	else: print(False)
	print(query)


def test_parent_generate_report_data():
	report = CountPeriodReport(START_TIME, END_TIME)
	query = report.generate_report_data()
	print('Check type of result - list')
	if type(query) is list: print(True)
	else: print(False)

	print('Check for length of list - > 0')
	if len(query) > 0: print(True)
	else: print(False)

	print('Check for schema of a result item - tuple and 2')
	if type(query[-1]) is tuple and len(query[-1]) == 2: print(True)
	else: print(False)

	print('Check for type of result items - str and int')
	if type(query[-1][0]) is str and type(query[-1][1]) is int: print(True)
	else: print(False)
	print(query)


def test_report_generator_class():
	in_memory = CountPeriodReport(START_TIME, END_TIME)
	if in_memory.db == ':memory:': print(True)
	else: print(False)


# TESTING EVENT REPORTS
def test_event_period_report():
	report = EventPeriodReport(START_TIME, END_TIME)
	# report.db = DB_HOME_PATH
	query = report.select_query()
	result = report.generate_report_data()
	#print(query)
	#print(result)
	report.create_html_report(result, 'event_test')


def test_project_event_period_report():
	report = ProjectEventPeriodReport(START_TIME, END_TIME, 'PM')
	query = report.select_query()
	result = report.generate_report_data()
	print(query)
	print(result)
	#report.create_html_report(result, 'event_test')


def test_item_event_period_report():
	report = ItemEventPeriodReport(START_TIME, END_TIME, 'hov')
	query = report.select_query()
	result = report.generate_report_data()
	print(query)
	print(result)
	report.create_html_report(result, 'event_test')


# REPORTS TESTS
def test_period_report():
	report = PeriodReport(START_TIME, END_TIME)
	print(report.report_name)
	report.generate_report()


def test_period_project_report():
	report = ProjectPeriodReport(START_TIME, END_TIME, 'PM', report_format='event')
	print(report.report_name)
	report.generate_report()


def test_period_item_report():
	report = ItemPeriodReport(START_TIME, END_TIME, 'Jackpot', report_format='event')
	print(report.report_name)
	report.generate_report()

