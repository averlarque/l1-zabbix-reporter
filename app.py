from bottle import Bottle, run, static_file, request, redirect
from jinja2 import Environment, FileSystemLoader
from handlers import *
from report_templates import *
import os

# Init Bootle.py app
app = Bottle()

# Init Jinja2 environmemt
j2_env = Environment(loader=FileSystemLoader(temp_path))


# Render html-templates
def render(tpl, context):
	return j2_env.get_template(tpl).render(context)


# Report page controller
@app.route('/report')
def report():
	data = get_datetime()
	since = data.get('since')
	till = data.get('till')
	context = {'since_time': since[0], 'since_date': since[1],
	           'till_time': till[0], 'till_date': till[1]}
	return render('report.tpl', context)

# Report page receiver
@app.route('/report', method='POST')
def make_report():
	since = {
		'time': request.forms.get('since_time'),
		'date': request.forms.get('since_date')
	}
	till = {
		'time': request.forms.get('till_time'),
		'date': request.forms.get('till_date')
	}
	
	time_period = time_handler(since, till)
	
	report_type = request.forms.get('type')

	report_format = request.forms.get('format')

	report_class = request.forms.get('report_class')
    # Launch report generation
	if report_class == 'project':
		project = request.forms.get('project')
		reporter = ProjectPeriodReport(
			time_period[0], time_period[1], project,
			report_format=report_format, report_type=report_type
		)
		reporter.generate_report()
	elif report_class == 'item':
		item = request.forms.get('item')
		reporter = ItemPeriodReport(
			time_period[0], time_period[1], item,
			report_format=report_format, report_type=report_type)
		reporter.generate_report()
	else:
		reporter = PeriodReport(
			time_period[0], time_period[1], report_format=report_format,
			report_type=report_type)
		reporter.generate_report()
	return render('status.tpl', {'text': report_ok})


# Login page controller
@app.route('/login')
def login():
	try:
		data = p_load()
		if len(data) > 1:
			context = {'host': data['host'], 'user': data['user']}
		else:
			context = {'host': '', 'user': ''}
	except EOFError:
		context = {'host': '', 'user': ''}
	return render('login.tpl', context)


# Login page receiver
@app.route('/login', method='POST')
def do_login():
	dct = {'host': request.forms.get('host'),
		   'user': request.forms.get('username'),
	       'time': str(today)[:19]}
	password = request.forms.get('password')
	check = login_check(dct, password)
	# Check access to the host
	if check[0] is True:
		dct.update({'api': check[1]})
		p_handler(dct)
		os.environ['pass'] = password
		return render('status.tpl', {'text': login_ok.format(dct['user'])})
	else:
		return render('status.tpl', {'text': login_fail})


# Settings page controller
@app.route('/settings')
def settings():
	data = p_load()
	context = {'host': data.get('host'),
	           'user': data.get('user'),
	           'time': data.get('time'),
	           'api': data.get('api'),
	           'reports': report_folder_path}
	return render('settings.tpl', context)


# Reports folder opener
@app.route('/reports_folder')
def reports_folder():
	open_reports_folder()
	# Redirect back to the settings
	redirect('/settings')


# About page controller
@app.route('/about')
def about():
	context = {'name': 1}
	return render('about.tpl', context)


# Static files handler
@app.get('/static/<filename:path>')
def send_static(filename):
	return static_file(filename, root=static_path)

# 404 error handler
def error404(error):
	return render('status.tpl', {'text': e404})

# 500 error handler
def error500(error):
	return render('status.tpl', {'text': e500})


handler = {500: error500, 404: error404}

app.error_handler = handler

# run(app, host='localhost', port=8060, debug=True)

if __name__ == '__main__':
	port = 8060
	from threading import Thread
	app_thread = Thread(target=run, kwargs=dict(app=app, host='localhost', port=port))
	# Starting the app
	app_thread.start()
	# Open the web browser
	webbrowser.open('http://localhost:{0}/login'.format(port))


