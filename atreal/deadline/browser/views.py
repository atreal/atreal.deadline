# -*- coding: utf-8 -*-

from Products.Five import BrowserView
from DateTime.DateTime import DateTime
from zope.interface import implements

# Import Plone
from Products.CMFPlone import MessageFactory
mf = MessageFactory('atreal.deadline')

# Imports: atreal.deadline
from atreal.deadline.interfaces import IDeadlineable
from atreal.deadline.interfaces import IDeadlineProvider
from atreal.deadline.browser.viewlet import DeadlineViewlet


class DeadlineProvider(BrowserView):

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
        return self._render_viewlet()

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

        day, month, year = deadline.split('/')
        deadline = "%s/%s/%s %s:%s" % (month, day, year, hour, minute)
        self.object.setDeadline(DateTime(deadline))
        self.object.setComment(comment)
        self.object.addHistoryEntry()

        return self._render_viewlet()

    def _render_viewlet(self):
        """ """
        viewlet = DeadlineViewlet(self.context, self.request, None, None).__of__(self.context)
        viewlet.update()
        return viewlet.render()
