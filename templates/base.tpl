  <!DOCTYPE html>
  <html>
    <head>
      <title>{% block title %} {% endblock title %}</title>
      <!--Import materialize.css-->
      <link type="text/css" rel="stylesheet" href="static/materialize.min.css"  media="screen,projection"/>
      {% block add_css %} {% endblock add_css %}
      <!--Let browser know website is optimized for mobile-->
      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    </head>

    <body>

      <div class="navbar">
        <nav>
          <div class="nav-wrapper">
            <a href="#!" class="brand-logo center">L1 Zabbix Reporter</a>
          </div>
        </nav>
      </div>
      <div class="row">
          <ul class="tabs row">
            {% block tabs %}
            <li class="tab col s4"><a class="active" target="_self" href="/report">Reporting</a></li>
            <li class="tab col s4"><a target="_self" href="/settings">Settings</a></li>
            <li class="tab col s4"><a target="_self" href="/about">About</a></li>
            {% endblock tabs %}
          </ul>
      </div>
      {% block content %}
      {% endblock content %}

      <!--Import jQuery before materialize.js-->
      <script type="text/javascript" src="static/jquery-2.1.1.min.js"></script>
      <script type="text/javascript" src="static/materialize.min.js"></script>
      <script type="text/javascript" src="static/report.js"></script>
    </body>
  </html>