from zope.component import queryUtility
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.layout.viewlets import ViewletBase
from Products.statusmessages.interfaces import IStatusMessage

from atreal.deadline.interfaces import IDeadline
#from atreal.deadline.browser.controlpanel import IDeadlineSchema

class DeadlineViewlet(ViewletBase):
    
    def update(self):
        """ """
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


