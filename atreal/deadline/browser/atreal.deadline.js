
function debug (value){
    alert(value);
}; 

//var deadline_3rd_party_scripts = false;

function displayDeadlineForm() {
    if (jq("#deadline-form").is(":hidden")) {
        //if (!deadline_3rd_party_scripts) {
        //    var site_url = jq("#deadline-display").attr('class') 
        //    jq.getScript(site_url + '/jscalendar/calendar_stripped.js');
        //    jq.getScript(site_url + '/jscalendar/calendar-en.js');
        //    deadline_3rd_party_scripts = true;
        //}
        jq("#deadline-form").slideDown("slow");
    }
    else {
        jq("#deadline-form").slideUp("slow");
    }
};

function displayDeadlineHistory() {
    if (jq("#deadline-history").is(":hidden")) {
        jq("#deadline-history").slideDown("slow");
    }
    else {
        jq("#deadline-history").slideUp("slow");
    }
};

function deleteDeadline() {
    target_url = jq(this).parent().attr("class") + '/@@deadline_provider/deleteDeadline'
    jq.get(target_url);
    if (jq("#deadline-form").is(":visible")) {
        jq("#deadline-form").slideUp("slow");
    }
    jq(".deadline span.dl-add").show();
    jq(".deadline span.dl-modify").hide();
    jq(".deadline span.dl-date").hide();
    jq(".deadline span.dl-comment").hide();
    jq(".deadline img.dl-arrow").hide();
    jq(".deadline span.dl-defaultmessage").show();
    jq(this).hide();
};

function initializeDeadline() {
    jq(".deadline span.dl-add").click(displayDeadlineForm);
    jq(".deadline span.dl-modify").click(displayDeadlineForm);
    jq(".deadline span.dl-history").click(displayDeadlineHistory);
    jq(".deadline span.dl-delete").click(deleteDeadline);

};

function initializeDatePicker() {
    jq('input.calendarInput').datepicker({showButtonPanel: true, dateFormat:'dd/mm/yy'});
    jq('input.calendarInput').each(function(f) {
            this.readonly = '1';
    });
};

jq(initializeDeadline);
jq(document).ready(initializeDatePicker);
