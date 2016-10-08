$(document).ready(function(){
	$("#project_class").click(function(){
        $("#project_name").prop("disabled", false);
        $("#item_name").prop("disabled", true);
    });

    $("#item_class").click(function(){
    	$("#item_name").prop("disabled", false);
    	$("#project_name").prop("disabled", true);
    });

    $("period_class").click(function(){
    	$("#item_name").prop("disabled", true);
    	$("#project_name").attr("disabled", true);
    });

    $('.collapsible').collapsible({
      accordion : false // A setting that changes the collapsible behavior to expandable instead of the default accordion style
    });
});