from plone.indexer.decorator import indexer
from zope.component.exceptions import ComponentLookupError

from dateable.kalends import IEvent

from atreal.deadline.interfaces import IDeadlineable, IDeadlineAware

@indexer(IDeadlineAware)
def eventStart_indexer(object):
  if object.portal_type=="Event":
    return object.start()
  try:
    obj = IEvent(object)
    start = obj.start()
    if not start:
      raise AttributeError
    return start
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError


@indexer(IDeadlineAware)
def eventEnd_indexer(object):
  if object.portal_type=="Event":
    return object.end()
  try:
    obj = IEvent(object)
    end = obj.end()
    if not end:
      raise AttributeError
    return end
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError


@indexer(IDeadlineAware)
def eventType_indexer(object):
  if object.portal_type=="Event":
    return object.getEventType()
  try:
    obj = IEvent(object)
    eventType = obj.getEventType()
    if not eventType:
      raise AttributeError
    return eventType
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError
  
  
@indexer(IDeadlineAware)  
def deadline_indexer(object):
  try:
    obj = IDeadlineable(object)
    deadline = obj.getDeadline()
    if not deadline:
      raise AttributeError
    return deadline
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError
