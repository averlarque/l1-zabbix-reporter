import pickle
import os
import sys
import subprocess
from pyzabbix import ZabbixAPI
from datetime import datetime
from pathlib import PurePath


root_path = os.getcwd()
pure_path_templates = PurePath(root_path).joinpath('templates')
temp_path = str(pure_path_templates)
static_path = str(pure_path_templates.joinpath('static'))
today = datetime.now()


def open_reports_folder():
	report_folder_path = str(PurePath(root_path).joinpath('reports'))
	if sys.platform == 'darwin':
		subprocess.Popen(['open', report_folder_path])
	elif sys.platform == 'linux2':
		subprocess.Popen(['xdg-open', report_folder_path])
	elif sys.platform == 'win32':
		subprocess.Popen(['explorer', report_folder_path])


def get_hours():
	hours = []
	for x in range(24):
		if x < 10:
			h = '0' + str(x)
			hours.append(h)
		else:
			hours.append(str(x))
	return hours


def get_minutes():
	minutes = []
	for x in range(60):
		if x < 10:
			m = '0' + str(x)
			minutes.append(m)
		else:
			minutes.append(str(x))
	return minutes


def get_dates():
	if 9 < today.hour < 21:
		since_date = today.date().strftime("%Y-%m-%d")
		till_date = since_date
	else:
		since_date = today.replace(day=today.day -1).strftime("%Y-%m-%d")
		till_date = today.date().strftime("%Y-%m-%d")
	return since_date, till_date


def p_handler(arg):
	with open('log_info.pk', 'wb') as f:
		pickle.dump(arg, f)


def p_load():
	with open('log_info.pk', 'rb') as fl:
		data = pickle.load(fl)
	return data


def login_check(cred, password):
	try:
		ZabbixAPI(cred['host'], user=cred['user'], password=password)
		result = True
	except:
		result = False
	return result


def time_handler(since, till):
	since_date = since['date'].split('-')
	start_time = datetime(
		int(since_date[0]), int(since_date[1]), int(since_date[2]),
		hour=int(since['hour']), minute=int(since['minute'])
	)
	till_date = till['date'].split('-')
	till_time = datetime(
		int(till_date[0]), int(till_date[1]), int(till_date[2]),
		hour=int(till['hour']), minute=int(till['minute'])
	)
	return start_time, till_time

login_ok = '''Hi {0}! You are logged in your Zabbix account.\n
	Press button below to return for report creation.
'''

login_fail = '''
	Something went wrong. Please check your credentials and operability of a chosen
	Zabbix host and your credentials. \n
	Then try to login again in the Settings section.
'''

e404 = '''
	The page was not found. May be something went wrong or may be it's
	something wrong with you.\n
	Anyway, please check the URL or try to reboot this app. \n
	If nothing helps, please send email to elijah.zaharov@gmail.com about the issue.
'''

report_ok = '''
	The report has been generated.
'''

e500 = '''
	<h3>500 error.</h3> \n
	\n
	<p>Something happened. May be it something terrible, but please keep patience
	and do not panic!\n</p>
	<p>Get back and check if you've done all right (not speaking about your life).
	Did you logged in your Zabbix account correctly, ah? \n
	Otherwise reboot the app and try again. \n</p>
	<p>If there is no hope insight, feel free to send email to elijah.zaharov@gmail.com with
	a description of an issue.\n</p>

'''
