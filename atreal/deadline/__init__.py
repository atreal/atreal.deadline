print "================================================"
print "atReal : ARDeadline"
print "================================================"

from Products.CMFCore.permissions       import setDefaultRoles
from Products.CMFCore.DirectoryView     import registerDirectory
from Products.ARDeadline.config  import *

# register skin directories so they can be added to portal_skins
registerDirectory('skins', GLOBALS)
