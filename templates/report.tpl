{% extends 'base.tpl' %}

{% block title %}
  L1 Zabbix Reporter - Report
{% endblock title %}

{% block add_css %}
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
{% endblock add_css %}

  
{% block content %}
  <div class="row" id="reports">

    <div class="container">
    
    <form action="/report" method="post">
      <!-- Time period section -->
      <h5>Time Period</h5>

      <div class="col s6">
        <span class="col s12">Start time:</span>
        <!-- Since time input -->
        <div class="input-field col s4 browser-default">
          <i class="material-icons prefix">schedule</i>
          <input type="time" name="since_time" value="{{since_time}}" style="text-align:center;" required>
        </div>
        <!-- Since date input -->
        <div class="input-field col s6 offset-s1">
          <i class="material-icons prefix">today</i>
          <input type="date" name="since_date" value="{{since_date}}" style="text-align:center;" required>
        </div>
      </div>

      <div class="col s6">
        <span class="col s12">End time:</span>
        <!-- Till time input -->
        <div class="input-field col s4">
          <i class="material-icons prefix">schedule</i>
          <input type="time" name="till_time" value="{{till_time}}" style="text-align:center;"  required>
        </div>
        <!-- Till date input -->
        <div class="input-field col s6 offset-s1">
          <i class="material-icons prefix">today</i>
          <input type="date" name="till_date" value="{{till_date}}" style="text-align:center;" required>
        </div>
        
      </div>
       
      <h5>Report Configuration</h5>
        <div class="row">
          <!-- General report -->
          <div class="col s12" id="period_report">
            <input class="with-gap" name="report_class" type="radio" id="period_class" value="period" checked  />
            <label for="period_class">General report on a specified period</label>
          </div>
          <!-- Project report -->
          <div class="col s6 " id="project_report">
            <input class="with-gap" name="report_class" type="radio" id="project_class" value="project" />
            <label for="project_class">Report on a specific project during the time 
            period</label>
          </div>

          <div class="col s6">
            <input type="text" name="project", placeholder="Project name" id="project_name" disabled required>      
          </div>
          <!-- Item report-->
        <div class="col s6" id="item_report">
          <input class="with-gap" name="report_class" type="radio" id="item_class" value="item"  />
          <label for="item_class">Report on a specific item/app/host diring the time period </label>
        </div>

        <div class="col s6">
            <input type="text" name="item", placeholder="Item/app/host title" id="item_name" disabled required>      
        </div>
      </div>
        

        <!-- Report formats -->
        
          <div class="row">
            <div class="col s6 input-field">
              <select class="browser-default" name="format" >
                <option value="count" selected>Show count of alert</option>
                <option value="event">Show timing of alerts</option>
              </select>
            </div>
            <div class="col s6 input-field">
              <select class="browser-default" name="type" >
                <option value="txt" selected>Create txt report</option>
                <option value="html">Create html report</option>
              </select>
            </div>
          </div>
        
        <div class="row">
          <input class="btn waves-effect waves-light col s2" type="submit" value="GENERATE">
        </div>
       
      </form>
    </div>
  </div>
      {% endblock content %}
      
     

