{% extends 'base.tpl' %}

    {% block title %}
        Zabbix Reporter L1 - Login Settings
    {% endblock title %}

	{% block tabs %}
            <li class="tab col s4"><a target="_self" href="/report">Reporting</a></li>
            <li class="tab col s4"><a class="active" target="_self" href="/login">Settings</a></li>
            <li class="tab col s4"><a target="_self" href="/about">About</a></li>
    {% endblock tabs %}

	{% block content %}
	<div class="container" id="settings">
            <form action="/login" method="post">
                Zabbix host: <input name="host" type="text" value="{{host}}" />
                Username: <input name="username" type="text" value="{{user}}" />
                Password: <input name="password" type="password" />
                <button class="btn waves-effect waves-light" type="submit" value="action">Submit
    
                </button>
            </form>
     </div>
	{% endblock content %}