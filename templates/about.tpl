{% extends 'base.tpl' %}

{% block title %}
	L1 Zabbix Reporter - About
{% endblock title %}

{% block tabs %}
            <li class="tab col s4"><a target="_self" href="/report">Reporting</a></li>
            <li class="tab col s4"><a target="_self" href="/settings">Settings</a></li>
            <li class="tab col s4"><a class="active" target="_self" href="/about">About</a></li>
{% endblock tabs %}

{% block content %}
<div class="row">
	<div class="container">
		<ul class="collapsible" data-collapsible="accordion">
    		<li>
      			<div class="collapsible-header"><h5>How to install it?</h5></div>
      			<div class="collapsible-body">
      				<p>You can clone and run this git repository or compile it to exe with PyInstaller library.</p>
      			</div>
    		</li>
    		<li>
      			<div class="collapsible-header"><h5>How to use it?</h5></div>
      			<div class="collapsible-body">
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
      			</div>
    		</li>
    		<li>
      			<div class="collapsible-header"><h5>How it works?</h5></div>
      			<div class="collapsible-body">
      				<p>The script refers to the API of the Zabbix Server and takes all events occurred during the time period. In this case, an <i>Event</i> is the case reported by host's trigger which is send to notify stakeholders about the issue. It is the simplest way to extract data from Zabbix server. If this functionality is disabled, the script won't get any data to report. <br> Then the inmemory sqlite database is created in order to parse and calculate these data and convert all that in a file. These report files are stored at <b>script_folder/reports/</b>. These files should be managed manually.</p>
      			</div>
    		</li>
    		<li>
      			<div class="collapsible-header"><h5>Does it work only on Windows OS?</h5></div>
      			<div class="collapsible-body">
      				<p>It also should work on the other platforms with Python 3.5 support as a major requirement. For correct displaying the latest Google Chrome is preferred.</p>
      			</div>
    		</li>
    		<li>
      			<div class="collapsible-header"><h5>Can it work with the newest version of Zabbix?</h5></div>
      			<div class="collapsible-body">
      				<p>It should work but I'm not sure as I have no possibility to test it on the newest Zabbix versions.</p>
      			</div>
    		</li>
    		<li>
      			<div class="collapsible-header"><h5>For conclusion...</h5></div>
      			<div class="collapsible-body">
      				<p>Please do not overload your Zabbix server as we cannot predict possible impact if you decide to dump data for long periods of time with many events. It can lead to a downtime of the server. So just make reports not more than 2 days from the current time. Otherwise, there is no any guarantee and I will not be responsible for possible troubles.</p>
      				</div>
    		</li>
  		</ul>
  		</div>
</div>
{% endblock content %}