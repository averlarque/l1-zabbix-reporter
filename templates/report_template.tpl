<!DOCTYPE html>
<html>
<head>
	<title> L1 Zabbix report - {{file_name}}</title>
</head>
<body>
	<div>
		<p>
		{% for line in general_report_data %}
			{{line}}<br>
		{% endfor %}
		</p>
	</div>
	<div>
		<ul type="None">
		{% if type == '0' %}
			{% for item in report_data %}
				<li>{{item}}</li>
			{% endfor %}
		{% else %}
			{% for item, value in report_data.items() %}
				<ul type="None"><strong>{{item}}</strong>
				{% for time in value %}
					<li>{{time}}</li>
				{% endfor %}	
				</ul>
			{% endfor %}
		{% endif %}
	</ul>
	
	</div>
</body>
</html>






