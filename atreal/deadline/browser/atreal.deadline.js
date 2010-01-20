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

function displayDeadlineForm() {
    //if (jq("#deadline-form").is(":hidden")) {
    jq("#deadline-form").slideDown(1000);
    //}
    //else {
        //jq("#deadline-form").hide();
    //}
};

function initializeDeadline() {
    //jq('#deadline').click(alert('yo!'))
    jq("#deadline span.add").click(displayDeadlineForm)
};

jq("#deadline-form").hide();
displayDeadlineForm();
//jq(initializeDeadline);
