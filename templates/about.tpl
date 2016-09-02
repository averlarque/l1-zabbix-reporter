{% extends 'base.tpl' %}

{% block title %}
	Zabbix Reporter L1 - About
{% endblock title %}

{% block tabs %}
            <li class="tab col s4"><a target="_self" href="/report">Reporting</a></li>
            <li class="tab col s4"><a target="_self" href="/login">Settings</a></li>
            <li class="tab col s4"><a class="active" target="_self" href="/about">About</a></li>
{% endblock tabs %}

{% block content %}
<div class="row">
	<div class="container">
		<h4>How to install it?</h4>
		<p>Just download the archive and unzip it where you want on your PC. Then open the folder and click on zbx_reporter.exe file. The script will up the local web-server and open a web page in your default-stated browser. In addition, yes, it preferably should be Google Chrome not from the Mesozoic.</p>

		<h4>How to use it?</h4>
		<p>After launching the script you will be automatically redirected to the login page, where you are to fill in your Zabbix host address and login information. The host and username values will be saved for convenience of further usage. Your password is not stored in, so you must use your password every session.<br>
		<b>It is important, because the script will not work without every-launch-stated-password and you will receive a bunch of 500 errors. </b>
		<br>
		After choose the time period for your report and its class. <i>General report</i> just calculates all alerts for required period. <i>Project report</i> counts only alerts that belong to a specific project. <i>Item report</i> includes only alerts that contain denoted aliases or app/host/whatever item in the title of alerts.
		<br>
		As the project reports, it parses alert titles trying to find results with the denoted stuff. It works well only in case when all (or most of alerts) follow this template:<br>
		<b>[project]: [host and name of alert]</b> <br> 
		<i>So the project report parses first part of alert title and the item report parses the remains.</i>
		<br>
		Then you choose report type. Count of alerts is like alert titles with number of these alerts occurred during the report time period.<br>
		<b>[title]: x[number]</b> <br>
		Timing of alerts denote title of alerts and exact time when the occurred during the report time.<br>
		<b>[title]: [time1, time2, etc]</b><br>
		After it you are supposed to choose report format as txt or html file. After the report making it will be opened automatically in your default browser or Notepad (or whatever you use as a text editor). <br>
		(Please be notified that html-reports sucks. No kidding, just check if you want). <br>
		Finally press Generate button and wait some time while a report is generating. It depends on your RAM and the scope of a report - usually it takes not so much time. After close a tab and terminate the console window, which denotes activities of a local web-server, or continue the session.
		</p>

		<h4>How it works?</h4>
		Easy peasy. The script refers to Zabbix API of denoted host with your credentials and takes all events occurred during the time period. In this case, an <i>Event</i> is the case reported by host's trigger which is send to notify stakeholders about the issue. It is the simplest way to extract data from Zabbix server. If this functionality is disabled, the script won't get any data to report. <br> Then the inmemory sqlite database is created in order to parse and calculate these data and convert all that in a file. These report files are stored at <b>script_folder/reports/</b>. These files should be managed manually. 

		<h4>Does it work only on Windows OS?</h4>
		<p>The code itself was written as multiplatformic (not sure, if this adjective exists in the language) in the way as Python is. However, it has been compiled as Windows executable. Therefore, if you want to launch the script on Mac or Linux just address me vie email (elijah.zaharov@gmail.com) and I will recompile the script.</p>

		<h4>Can it work with the newest version of Zabbix?</h4>
		<p>Honestly, I am not sure about it. I am definitely certain about 2.2.3 and higher until the third major version. If you tested the newest ones and have found some troubles, please feel free to address me this issue.</p>

		<h4>For conclusion...</h4>
		<p>Please do not overload your Zabbix server as we cannot predict possible impact if you decide to dump data for long periods of time with many events. It can lead to a downtime of the server. So just make reports not more than 2 days from the current time. Otherwise, there is no any guarantee and I will not be responsible for possible troubles.</p>
	</div>
</div>
{% endblock content %}