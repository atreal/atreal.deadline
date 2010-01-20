from zope.component.exceptions import ComponentLookupError

from Products.CMFPlone.CatalogTool import registerIndexableAttribute

from DateTime import DateTime

#from p4a.calendar.interfaces import IEvent

from zope.interface import implements
from BTrees.OOBTree import OOBTree
from zope.app.annotation.interfaces import IAnnotations
from Products.CMFCore.utils import getToolByName
from plone.indexer.decorator import indexer

from atreal.deadline.interfaces import IDeadlineable


class ToDeadlineableObject( object ):

  implements(IDeadlineable)

  def __init__(self, context):
    self.key         = 'transition_deadline'
    self.context     = context
    self.annotations = IAnnotations(context)
    if not self.annotations.get(self.key, None):
      self.annotations[self.key] = OOBTree()
  
  def setDeadline(self, deadline):
    if deadline:
      deadline= DateTime(deadline)
    self.annotations[self.key]['deadline'] = deadline
    self.context.reindexObject()
  
  def getDeadline(self):
    if 'deadline' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['deadline']

  def setNextDeadline(self, deadline):
    if deadline:
      deadline = DateTime(deadline)
    self.annotations[self.key]['nextDeadline'] = deadline
  
  def getNextDeadline(self):
    if 'nextDeadline' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['nextDeadline']
  

  def storeDeadlineInWorkflowHistory(self):
    deadline=self.getDeadline()
    for wfid, wflow in self.context.workflow_history.items():
      wflow[-1]['deadline']=deadline
    self.setDeadline(self.getNextDeadline())
    self.setNextDeadline(False)
    
  def setResponsible(self, responsible):
    self.annotations[self.key]['responsible'] = responsible
    self.context.reindexObject()

  def getResponsible(self):
    if 'responsible' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['responsible']

#
#class DeadlineableToEventObject( object ):
#
#  implements( IEvent )
#  
#  def __init__(self, context):
#    self.context = IDeadlineable(context)
#
#  def start(self):
#    return self.context.getDeadline()
#
#  def end(self):
#    return self.context.getDeadline()
#  
#  def getEventType(self):
#    return ("Deadline")
