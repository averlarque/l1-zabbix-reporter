{% extends 'base.tpl' %}

{% block title %}
	L1 Zabbix Reporter - Settings
{% endblock title %}

{% block tabs %}
	<li class="tab col s4"><a target="_self" href="/report">Reporting</a></li>
    <li class="tab col s4"><a target="_self" class="active" href="/settings">Settings</a></li>
    <li class="tab col s4"><a target="_self" href="/about">About</a></li>
{% endblock tabs %}

{% block content %}
	<div class="container">
		<div class="row">
			
			<div class="col s4 m4 l4 card">
				<div class="card-content">
					<span class="card-title">User Info</span>
					<h6>Username: {{user}}</h6>
					<h6>Last login: {{time}}</h6>
					<div class="card-action">
              			<a href="/login">Re-login</a>
            		</div>
				</div>
			</div>
			<div class="col s4 m4 l4 card">
				<div class="card-content">
					<span class="card-title">Zabbix Info</span>
					<h6>Host: {{host}}</h6>
					<h6>API version: {{api}}</h6>
					<div class="card-action">
              			<a href="{{host}}">Go to Host</a>
            		</div>
				</div>
			</div>
			<div class="col s4 m4 l4 card">
				<div class="card-content">
					<span class="card-title">Reports</span>
					<h6>Reports folder:</h6>
					<h6>{{reports}}</h6>
					<div class="card-action">
              			<a href="/reports_folder">Check Reports</a>
            		</div>
				</div>
			</div>

		</div>
		<div class="row">
      		<div class="col s12">
	        	<div class="card-panel" style="background-color: #757575;">
	          		<span class="white-text">
	          		L1 Zabbix Reporter - version 1.0. Released in October 2016. This project is under the <a href="https://github.com/averlarque/l1-zabbix-reporter/blob/master/LICENSE">MIT License</a>. <br>You can check and contribute to the source code on <a href="https://github.com/averlarque/l1-zabbix-reporter">Github</a>. In case of any problems please report them <a href="https://github.com/averlarque/l1-zabbix-reporter/issues">here</a>. 
	          		</span>
	        	</div>
      		</div>
    	</div>
	</div>
{% endblock content %}