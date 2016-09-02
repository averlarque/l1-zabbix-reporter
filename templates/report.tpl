{% extends 'base.tpl' %}

{% block title %}
  Zabbix Reporter L1 - Report
{% endblock title %}
  
{% block content %}
  <div class="row" id="reports">
  <!-- Statement -->
    <div class="row">
      <div class="col s8 offset-s2">
        <div class="card-panel teal">
          <span class="white-text">Before making a report please make sure that you have
          submitted your Zabbix login info in <a href="/login">Settings</a>. If you have any questions, please check the About section. In case of any issues please send its description to elijah.zaharov@gmail.com. Thanks!
          </span>
        </div>
      </div>
    </div>

    <div class="container">
    <!-- Time period section -->
    <form action="/report" method="post">
      <div class="section">
        <h5>Time Period</h5>
        <div class="col s6">

            <div class="col s6">
              <div class="col s6">
                <select class="browser-default" name="since_hour" required>
                  <option value="" disabled selected>Hours</option>
                  {% for h in hours %}
                  <option value="{{h}}">{{h}}</option>
                  {% endfor %}
                </select>
              </div>
              <div class="col s6">
                <select class="browser-default" name="since_min" required>
                  <option value="" disabled selected>Minutes</option>
                  {% for m in mins %}
                  <option value="{{m}}">{{m}}</option>
                  {% endfor %}
                </select>
              </div>
            </div>

            <div class="col s6">
              <input type="date" name="since_date" value="{{since_date}}" required>
            </div>
          
        </div>
        <div class="col s6">
          
            <div class="col s6">
              <div class="col s6">
                <select class="browser-default" name="till_hour" required>
                  <option value="" disabled selected>Hours</option>
                  {% for h in hours %}
                  <option value="{{h}}">{{h}}</option>
                  {% endfor %}
                </select>
              </div>
              <div class="col s6">
                <select class="browser-default" name="till_min" required>
                  <option value="" disabled selected>Minutes</option>
                  {% for m in mins %}
                  <option value="{{m}}">{{m}}</option>
                  {% endfor %}
                </select>
              </div>
            </div>
            <div class="col s6">
              <input type="date" name="till_date" value="{{till_date}}" required>
            </div>
          
        </div>
      </div>
      <!-- Report type -->
      <div class="divider"></div>
        <div class="section">
          <h5>Report configuration</h5>
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
          <!--<input class="btn waves-effect waves-light right" type="reset" value="RESET">-->
        </div>
       </div> 
      </form>
    </div>
  </div>
      {% endblock content %}
      
     

