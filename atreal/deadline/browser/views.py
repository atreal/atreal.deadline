import time

# Imports: Zope
#from Acquisition import aq_inner
from Products.Five  import BrowserView
from DateTime.DateTime import DateTime
#from zope.event import notify
from zope.interface import implements

# Import Plone
from Products.CMFPlone import MessageFactory
mf = MessageFactory('atreal.deadline')

# Imports: atreal.deadline
from atreal.deadline.interfaces import IDeadlineable
from atreal.deadline.interfaces import IDeadlineProvider


class DeadlineProvider( BrowserView ):

    implements(IDeadlineProvider)
    
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.object = IDeadlineable(context, None)
    
    def getDeadline(self):
        """
        """
        return self.object.getDeadline()
    
    def setDeadline(self):
        """
        """
        deadline = self.request['Deadline']
        self.object.setDeadline(deadline)

    def deleteDeadline(self):
        """
        """
        self.object.deleteDeadline()
    
    def getComment(self):
        """
        """
        return self.object.getComment()
    
    def setComment(self):
        """
        """
        comment = self.request['comment']
        self.object.setComment(comment)
    
    def getHistory(self):
        """
        """
        return self.object.getHistory()
    
    def submitDeadlineForm(self):
        """
        """
        deadline = self.request['Deadline']
        hour = self.request['Deadline_hour']
        minute = self.request['Deadline_minute']
        comment = self.request['comment']
        
        if deadline:
            day,month,year = deadline.split('/')
            deadline = "%s/%s/%s %s:%s" % (month, day, year, hour, minute)
            #deadline = time.strptime("%s %02d:%02d" %\
            #                         (deadline,int(hour),int(minute)),
            #                         '%d/%m/%Y %H:%M')[:5]
            self.object.setDeadline(DateTime(deadline))
            if comment:
                self.object.setComment(comment)
            self.object.addHistoryEntry()
        
        return self.request.RESPONSE.redirect("%s/view" % self.context.absolute_url())

