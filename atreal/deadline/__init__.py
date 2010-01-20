print "================================================"
print "atReal.deadline"
print "================================================"

from Products.CMFCore.permissions       import setDefaultRoles
from Products.CMFCore.DirectoryView     import registerDirectory
from atreal.deadline.config  import GLOBALS

# register skin directories so they can be added to portal_skins
# registerDirectory('skins', GLOBALS)
