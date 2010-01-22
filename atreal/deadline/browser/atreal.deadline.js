/*
 * This is the code for the dropdown menus. It uses the following markup:
 *
 * <dl class="actionMenu" id="uniqueIdForThisMenu">
 *   <dt class="actionMenuHeader">
 *     <!-- The following a-tag needs to be clicked to dropdown the menu -->
 *     <a href="some_destination">A Title</a>
 *   </dt>
 *   <dd class="actionMenuContent">
 *     <!-- Here can be any content you want -->
 *   </dd>
 * </dl>
 *
 * When the menu is toggled, then the dl with the class actionMenu will get an
 * additional class which switches between 'activated' and 'deactivated'.
 * You can use this to style it accordingly, for example:
 *
 * .actionMenu.activated {
 *   display: block;
 * }
 *
 * .actionMenu.deactivated {
 *   display: none;
 * }
 *
 * When you click somewhere else than the menu, then all open menus will be
 * deactivated. When you move your mouse over the a-tag of another menu, then
 * that one will be activated and all others deactivated. When you click on a
 * link inside the actionMenuContent element, then the menu will be closed and
 * the link followed.
 *
 */

function debug (value){
    alert(value);
}; 

var deadline_3rd_party_scripts = false;

function displayDeadlineForm() {
    if (jq("#deadline-form").is(":hidden")) {
        if (!deadline_3rd_party_scripts) {
            var site_url = jq("#deadline-display").attr('class') 
            jq.getScript(site_url + '/jscalendar/calendar_stripped.js');
            jq.getScript(site_url + '/jscalendar/calendar-en.js');
            deadline_3rd_party_scripts = true;
        }
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
    if (jq("#deadline-form").is(":visible")) {
        jq("#deadline-form").slideUp("slow");
    }
    jq(".deadline span.dl-add").show();
    jq(".deadline span.dl-modify").hide();
    jq(this).hide();
};

function initializeDeadline() {
    jq(".deadline span.dl-add").click(displayDeadlineForm);
    jq(".deadline span.dl-modify").click(displayDeadlineForm);
    jq(".deadline span.dl-history").click(displayDeadlineHistory);
    jq(".deadline span.dl-delete").click(deleteDeadline);

};

jq(initializeDeadline);
