from DateTime import DateTime

from dateable.kalends import IEvent

from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from BTrees.OOBTree import OOBTree
from zope.annotation.interfaces import IAnnotations

from atreal.deadline.interfaces import IDeadlineable


class ToDeadlineableObject( object ):

  implements(IDeadlineable)

  def __init__(self, context):
    self.key         = self.__class__.__name__
    self.context     = context
    self.annotations = IAnnotations(context)
    if not self.annotations.get(self.key, None):
      self.annotations[self.key] = OOBTree()
  
  def setDeadline(self, deadline):
    if  not deadline:
      return
    deadline = DateTime(deadline)
    self.annotations[self.key]['deadline'] = deadline
    self.context.reindexObject(idxs=['deadline']) # XXX reindex only the right index
  
  def getDeadline(self):
    if 'deadline' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['deadline']

  def setComment(self, comment):
    if not comment:
      return
    self.annotations[self.key]['comment'] = comment
    self.context.reindexObject()
  
  def getComment(self):
    if 'comment' not in self.annotations[self.key]:
      return ''
    return self.annotations[self.key]['comment']

  def addHistoryEntry(self):
    """ """
    if 'history' not in self.annotations[self.key]:
      self.annotations[self.key]['history'] = []
    history = self.annotations[self.key]['history']
    if len(history) and (DateTime(self.getDeadline()) == history[-1][0]):
      # The deadline didn't change
      self.annotations[self.key]['history'][-1][1] = self.getComment()
    else:
      self.annotations[self.key]['history'].append([self.getDeadline(),
                                                 self.getComment()])

  def getHistory(self):
    """ """
    if 'history' not in self.annotations[self.key]:
      return []
    return self.annotations[self.key]['history']


class DeadlineableToEventObject( object ):

  def __init__(self, context):
    self.context = IDeadlineable(context)

  def start(self):
    return self.context.getDeadline()

  def end(self):
    return self.context.getDeadline()
  
  def getEventType(self):
    return ("Deadline")
   
  