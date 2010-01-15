# -*- coding: utf-8 -*-
#
# File: ARDeadline/interfaces.py
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


from zope.interface import Interface
from zope.app.event.interfaces import IObjectModifiedEvent


class IDeadlineAware( Interface ):
  """ marker interface """

class IDeadlineable( Interface ):
  
  def setDeadline( dueDate):
    """
    Sets the deadline of the next transition
    """
  
  def getDeadline( ):
    """
    Get the deadline of the next transition
    """

  def storeDeadlineInWorkflowHistory( ):
    """
    Store the current deadline in workflow history
    """
    
class IDeadlineProvider( Interface ):
  
  def setDeadline( dueDate):
    """
    Sets the deadline of the next transition
    """
  
  def getDeadline( ):
    """
    Get the deadline of the next transition
    """

  def setDeadlineAndTransition( ):
    """
    Sets the deadline of the next transition and traverse_to the transition cpy
    """
  
  def getResponsible( ):
    """
    """
  
  def setResponsible( ):
    """
    """

  def getPossibleResponsible( ):
    """
    Return all possible responsible users for this object (called from deadline_view.pt)
    """
  
  def setDeadlineAndResponsible(self):
    """
    Sets the deadline of the next transition and the responsible for this object (called from deadline_view.pt)
    """
    

  def submitDeadlineForm(self):
    """
    Handles the form of deadline_view.pt
    """