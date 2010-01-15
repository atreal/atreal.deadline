# -*- coding: utf-8 -*-
#
# File: ARDeadLine/views.py
#
# Copyright (c) 2007 atReal
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

"""
$Id$
"""

__author__ = """Jean-Nicolas Bès <contact@atreal.net>"""
__docformat__ = 'plaintext'
__licence__ = 'GPL'

# Imports: Zope
from Acquisition import aq_inner
from Products.Five  import BrowserView
from zope.event import notify
from zope.interface import implements

# Imports: CMF
from Products.CMFCore.utils import getToolByName

# Import Plone
from Products.CMFPlone import MessageFactory
mf = MessageFactory('eventsubscription')

# Imports: ARDeadline
from Products.ARDeadline.interfaces import IDeadlineable
from Products.ARDeadline.interfaces import IDeadlineProvider


class DeadlineProvider( BrowserView ):

  implements( IDeadlineProvider )

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
    deadline = self.context.REQUEST['Deadline']
    self.object.setDeadline(deadline)
  
  def setDeadlineAndTransition(self):
    """
    """
    deadline = self.context.REQUEST['Deadline']
    self.object.setNextDeadline(deadline)
    self.request.RESPONSE.redirect(self.request.get("orig_url"))
    
  def getResponsible(self):
    """
    """
    return self.object.getResponsible()
  
  def setResponsible(self):
    """
    """
    responsible = self.context.REQUEST['Responsible']
    self.object.setResponsible(responsible)

  def getPossibleResponsible(self):
    """
    """
    infos = []
    pmt = getToolByName(self, 'portal_membership')
    infos = [dict(
      id=member.id,
      fullname=member.getProperty('fullname',None),
      email=member.getProperty('email',None)
    ) for member in pmt.listMembers()]
    infos[0:0]=[dict(
        id='',
        fullname='Aucun',
        email='contact@atreal.net',
    )]
    return infos

  #def setDeadlineAndResponsible(self):
  #  """
  #  """
  #  deadline = self.context.REQUEST['Deadline']
  #  responsible = self.context.REQUEST['Responsible']
  #  self.object.setDeadline(deadline)
  #  self.object.setResponsible(responsible)
  #  msg="You successfully changed worklflow_deadline and workflow_responsible!"
  #  self.context.plone_utils.addPortalMessage(msg)
  #  self.request.RESPONSE.redirect(self.request.get("orig_url"))

  def submitDeadlineForm(self):
    """
    """
    deadline = self.context.REQUEST['Deadline']
    responsible = self.context.REQUEST['Responsible']
    comment = self.context.REQUEST['comment']
    workflow_action = self.context.REQUEST['workflow_action']
    
    if deadline == 'False':
        deadline = False
    
    wt = self.context.portal_workflow
    workflow_id =  wt.getChainFor(self.context)[0]
    
    current_deadline = self.object.getDeadline()
    workflow_state = wt.getInfoFor(self.context, 'review_state')
    
    if workflow_action!=workflow_state:
        ## workflow transition
        if deadline:
            self.object.setNextDeadline(deadline)
        wt.doActionFor(self.context, workflow_action, comment=comment)
    else:
        ## just a deadline change
        if deadline:
            self.object.setDeadline(deadline)
    self.object.setResponsible(responsible)
    msg="You successfully changed worklflow_deadline and workflow_responsible!"
    self.context.plone_utils.addPortalMessage(msg)
    self.request.RESPONSE.redirect(self.request.get("orig_url"))

