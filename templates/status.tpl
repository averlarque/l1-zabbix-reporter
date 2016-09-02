{% extends 'base.tpl' %}

{% block title %}
Zabbix Reporter L1 - Status Page
{% endblock title %}
	
	{% block tabs %} {% endblock tabs %}

	{% block content %}

	<div class="row">
		<div class="container">
			<p>{{text}}</p>
				<div>
					<a class="btn btn-large col s2" href="/report">TO REPORT</a>
					<a class="btn btn-large right" href="/login">TO SETTINGS</a>
				</div>
		</div>
	</div>

	{% endblock content %}