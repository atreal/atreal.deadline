Introduction
============

Adds a deadline to any plone content. The deadline adds a IEvent interface to
the object, making it compatible with calendars that are based on IEvent such
p4a.calendar. Dates are stored in an index, making them searchable.


TODO
----
 * Ajaxify the deadline save
 * Get rid of dateable.kalends.IEvent and implements standard IEvent interface
   instead
 * Control panel to select which CT provides deadline interface
 * Integrate deadline history in global history (? - f10w mentionned it)
 * Add index in alternative step to avoid reindexing at install time
