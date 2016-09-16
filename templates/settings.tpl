{% extends 'base.tpl' %}

{% block title %}
	Zabbix Reporter L1 - Settings
{% endblock title %}

{% block tabs %}
	<li class="tab col s4"><a target="_self" href="/report">Reporting</a></li>
    <li class="tab col s4"><a target="_self" class="active" href="/settings">Settings</a></li>
    <li class="tab col s4"><a target="_self" href="/about">About</a></li>
{% endblock tabs %}

{% block content %}
	<div class="container">
		<p> Zabbix host: {{host}} <br>
			Signed as: {{user}} <br>
			Login time: {{time}}
		</p>
		<a class="btn btn-large" href="/login">Re-Login</a>
		<a class="btn btn-large right" href="/reports_folder">Previous Reports</a>
	</div>
{% endblock content %}