from DateTime import DateTime

from zope.component import queryUtility
from zope.component import getMultiAdapter
from Acquisition import aq_inner, aq_parent
from AccessControl import getSecurityManager
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.layout.viewlets import ViewletBase
from Products.statusmessages.interfaces import IStatusMessage
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone import utils

from atreal.deadline.interfaces import IDeadlineable
#from atreal.deadline.browser.controlpanel import IDeadlineSchema

class DeadlineViewlet(ViewletBase):
    
    #def site_url(self):
    #    """ """
    #    return self.site_url
    
    def canModify(self):
        """ """
        if getSecurityManager().checkPermission('Modify portal content',
                                                self.context):
            return True
        return False

    def hasDeadline(self):
        """ """
        return True and self.deadline or False
    
    def getDeadline(self):
        """ """
        if not self.deadline:
            return self.deadline
        dl = self.deadline.strftime("%d/%m/%Y à %Hh%M")
        return dl

    def hasComment(self):
        """ """
        return True and self.comment or False
    
    def getComment(self):
        """ """
        return self.comment

    def getConfig(self):
        """ """
        return dict(
            deadline = self.hasDeadline() and self.deadline or DateTime(),
            comment = self.comment,
            show_hm = 1,
            show_ymd = 1,
            starting_year = 2010,
            ending_year = 2020,
        )
    
    def update(self):
        """ """
        super(DeadlineViewlet, self).update()
        self.deadlineProvider = getMultiAdapter((self.context, self.request),
                                            name=u'deadline_provider')
        self.deadline = self.deadlineProvider.getDeadline()
        self.comment = self.deadlineProvider.getComment()
        try:
            self.uniqueItemIndex = aq_inner(self).view._data['uniqueItemIndex']
        except:
            self.uniqueItemIndex = utils.RealIndexIterator(pos=0) # @@manage-viewlets or other
            
        #siteroot = queryUtility(IPloneSiteRoot)
        #conf = IDeadlineSchema(siteroot)
        #if not getattr(conf, 'actr_active', True):
        #    return
        #super(DeadlineViewlet, self).update()
        #actr = IDeadline(self.context)
        #try:
        #    actr.storeAccess()
        #except DeadlineError, e:
        #    IStatusMessage(self.request).addStatusMessage(e.args[0], type='error') 

    index = ViewPageTemplateFile("deadline.pt")      


