from DateTime import DateTime

from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFPlone import MessageFactory
_ = MessageFactory('atreal.deadline')


class DeadlineViewlet(ViewletBase):

    index = ViewPageTemplateFile("deadline.pt")
    
    def canModify(self):
        """ """
        if getSecurityManager().checkPermission('Deadline: Modify deadline',
                                                self.context):
            return True
        return False

    def hasDeadline(self):
        """ """
        return True and self.deadline or False
    
    def getHumanDeadline(self):
        """ """
        return self.deadline.strftime("%d/%m/%Y à %Hh%M")

    def getJqueryDeadline(self):
        """ """
        if not self.deadline:
            deadline = DateTime()
        else:
            deadline = self.deadline
        return deadline.strftime("%d/%m/%Y#%H#%M").split('#')

    def hasComment(self):
        """ """
        return True and self.comment or False
    
    def getComment(self):
        """ """
        return self.comment

    def hasHistory(self):
        """ """
        return True and self.history or False

    def getHistory(self):
        """ """
        for deadline, comment in self.history:
            yield dict(
                deadline = deadline.strftime("%d/%m/%Y à %Hh%M"),
                comment = comment,
            )

    def update(self):
        """ """
        super(DeadlineViewlet, self).update()
        self.deadlineProvider = getMultiAdapter((self.context, self.request),
                                            name=u'deadline_provider')
        self.deadline = self.deadlineProvider.getDeadline()
        self.comment = self.deadlineProvider.getComment()
        self.history = self.deadlineProvider.getHistory()


