
function debug (value){
    alert(value);
}; 

function displayDeadlineForm() {
    if (jq("#deadline-form").is(":hidden")) {
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

function addDeadline() {
    var url = jq('#deadline-form').attr('data-absolute_url');
    jq.ajax({
        url: url + '/@@deadline_management//submitDeadlineForm',
        type: 'POST',
        data: jq('#deadline-form form').serializeArray(),
        dataType: 'html',
        cache: false,
        success: function(data) {
            jq('#content-deadline').replaceWith(data);
            initializeDeadline();
            initializeDatePicker();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // debugger;
        }
    });
};


function deleteDeadline() {
    var url = jq('#deadline-form').attr('data-absolute_url');
    jq.ajax({
        url: url + '/@@deadline_management/deleteDeadline',
        type: 'POST',
        dataType: 'html',
        cache: false,
        success: function(data) {
            jq('#content-deadline').replaceWith(data);
            initializeDeadline();
            initializeDatePicker();
        },
        error: function(jqXHR, textStatus, errorThrown) {
            // debugger;
        }
    });
};

function initializeDeadline() {
    jq(".deadline span.dl-add").click(displayDeadlineForm);
    jq(".deadline span.dl-modify").click(displayDeadlineForm);
    jq(".deadline span.dl-history").click(displayDeadlineHistory);
    jq(".deadline span.dl-delete").click(deleteDeadline);
    jq('.deadline input[type=submit]').click(function(e){
        e.preventDefault();
        addDeadline();
    });
};

function initializeDatePicker() {
    jq('input.calendarInput').datepicker({showButtonPanel: true, dateFormat:'dd/mm/yy'});
    jq('input.calendarInput').each(function(f) {
            this.readonly = '1';
    });
};

jq(initializeDeadline);
jq(document).ready(initializeDatePicker);
