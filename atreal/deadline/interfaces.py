from zope.interface import Interface

class IDeadlineLayer( Interface ):
    """ Marker interface that defines a Zope 3 browser layer.
    """


class IDeadlineAware( Interface ):
  """ marker interface """


class IDeadlineable( Interface ):
  
  def setDeadline( dueDate):
    """ Sets the deadline of the next transition """
  
  def getDeadline( ):
    """ Get the deadline of the next transition """

  def setComment(self, comment):
    """ Set the comment """

  def getComment(self):
    """ Get the comment """
    
  def addHistoryEntry(self):
    """ Add a new entry in the deadline history """

  def getHistory(self):
    """ Get the deadline history """    


class IDeadlineProvider( Interface ):
  
  def setDeadline( dueDate):
    """
    Sets the deadline of the next transition
    """
  
  def getDeadline( ):
    """
    Get the deadline of the next transition
    """

  def getComment(self):
      """
      """
  
  def setComment(self):
      """
      """
  
  def getHistory(self):
      """
      """

  def submitDeadlineForm(self):
    """
    """