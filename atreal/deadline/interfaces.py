from zope.interface import Interface
from zope.app.event.interfaces import IObjectModifiedEvent

class IDeadlineLayer( Interface ):
    """ Marker interface that defines a Zope 3 browser layer.
    """


class IDeadlineAware( Interface ):
  """ marker interface """


class IDeadlineable( Interface ):
  
  def setDeadline( dueDate):
    """
    Sets the deadline of the next transition
    """
  
  def getDeadline( ):
    """
    Get the deadline of the next transition
    """

  def storeDeadlineInWorkflowHistory( ):
    """
    Store the current deadline in workflow history
    """


class IDeadlineProvider( Interface ):
  
  def setDeadline( dueDate):
    """
    Sets the deadline of the next transition
    """
  
  def getDeadline( ):
    """
    Get the deadline of the next transition
    """

  def setDeadlineAndTransition( ):
    """
    Sets the deadline of the next transition and traverse_to the transition cpy
    """
  
  def getResponsible( ):
    """
    """
  
  def setResponsible( ):
    """
    """

  def getPossibleResponsible( ):
    """
    Return all possible responsible users for this object (called from deadline_view.pt)
    """
  
  def setDeadlineAndResponsible(self):
    """
    Sets the deadline of the next transition and the responsible for this object (called from deadline_view.pt)
    """
    

  def submitDeadlineForm(self):
    """
    Handles the form of deadline_view.pt
    """