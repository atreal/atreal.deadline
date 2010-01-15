# -*- coding: utf-8 -*-
#
# File: ARDeadline/adapters.py
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

from zope.component.exceptions import ComponentLookupError

from Products.CMFPlone.CatalogTool import registerIndexableAttribute

from DateTime import DateTime

from p4a.calendar.interfaces import IEvent

from zope.interface import implements
from BTrees.OOBTree import OOBTree
from zope.app.annotation.interfaces import IAnnotations
from Products.CMFCore.utils import getToolByName
from Products.ARDeadline.interfaces import IDeadlineable


class ToDeadlineableObject( object ):

  implements( IDeadlineable )


  def __init__(self, context):
    self.key         = 'transition_deadline'
    self.context     = context
    self.annotations = IAnnotations(context)
    if not self.annotations.get(self.key, None):
      self.annotations[self.key] = OOBTree()
  
  def setDeadline(self, deadline):
    if deadline:
      deadline= DateTime(deadline)
    self.annotations[self.key]['deadline'] = deadline
    self.context.reindexObject()
  
  def getDeadline(self):
    if 'deadline' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['deadline']

  def setNextDeadline(self, deadline):
    if deadline:
      deadline = DateTime(deadline)
    self.annotations[self.key]['nextDeadline'] = deadline
  
  def getNextDeadline(self):
    if 'nextDeadline' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['nextDeadline']
  

  def storeDeadlineInWorkflowHistory(self):
    deadline=self.getDeadline()
    for wfid, wflow in self.context.workflow_history.items():
      wflow[-1]['deadline']=deadline
    self.setDeadline(self.getNextDeadline())
    self.setNextDeadline(False)
    
  def setResponsible(self, responsible):
    self.annotations[self.key]['responsible'] = responsible
    self.context.reindexObject()

  def getResponsible(self):
    if 'responsible' not in self.annotations[self.key]:
      return False
    return self.annotations[self.key]['responsible']

class DeadlineableToEventObject( object ):

  implements( IEvent )
  
  def __init__(self, context):
    self.context = IDeadlineable(context)

  def start(self):
    return self.context.getDeadline()

  def end(self):
    return self.context.getDeadline()
  
  def getEventType(self):
    return ("Deadline")

def eventStartIndexWrapper(object, portal, **kwargs):
  if object.portal_type=="Event":
    return object.start()
  try:
    obj = IEvent(object)
    start = obj.start()
    if not start:
      raise AttributeError
    return start
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError

registerIndexableAttribute('start', eventStartIndexWrapper)

def eventEndIndexWrapper(object, portal, **kwargs):
  if object.portal_type=="Event":
    return object.end()
  try:
    obj = IEvent(object)
    end = obj.end()
    if not end:
      raise AttributeError
    return end
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError

registerIndexableAttribute('end', eventEndIndexWrapper)

def eventTypeIndexWrapper(object, portal, **kwargs):
  if object.portal_type=="Event":
    return object.getEventType()
  try:
    obj = IEvent(object)
    eventType = obj.getEventType()
    if not eventType:
      raise AttributeError
    return eventType
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError

registerIndexableAttribute('getEventType', eventTypeIndexWrapper)
  
def deadlineIndexWrapper(object, portal, **kwargs):
  try:
    obj = IDeadlineable(object)
    deadline = obj.getDeadline()
    if not deadline:
      raise AttributeError
    return deadline
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError

registerIndexableAttribute('workflow_deadline', deadlineIndexWrapper)

def responsibleIndexWrapper(object, portal, **kwargs):
  try:
    obj = IDeadlineable(object)
    responsible = obj.getResponsible()
    if not responsible:
      raise AttributeError
    return responsible
  except (ComponentLookupError, TypeError, ValueError):
    # The catalog expects AttributeErrors when a value can't be found
    raise AttributeError

registerIndexableAttribute('workflow_responsible', responsibleIndexWrapper)
