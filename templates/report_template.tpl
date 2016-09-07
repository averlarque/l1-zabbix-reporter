{% extends 'base.tpl' %}

{% block title %}
Zabbix report - {{file_name}}
{% endblock title %}

{% block tabs %}
{% endblock tabs %}

{% block content %}
<div>
	{% for line in general_report_data %}
	{{line}}
	{% endfor %}
</div>
<div>
	<ul>
	{% if type == '0' %}
		{% for item in report_data %}
		<li>{{item}}</li>
		{% endfor %}
	{% else %}
		{% for item in report_data %}
			<ul>{{item}}
				{% for time in item.values() %}
					<li>{{time}}</li>
				{% endfor %}
			</ul>
		{% endfor %}
	{% endif %}
	</ul>
	
</div>
{% endblock content %}