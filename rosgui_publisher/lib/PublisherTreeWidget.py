#!/usr/bin/env python

# Copyright (c) 2011, Dorian Scholz, TU Darmstadt
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above
#     copyright notice, this list of conditions and the following
#     disclaimer in the documentation and/or other materials provided
#     with the distribution.
#   * Neither the name of the TU Darmstadt nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import roslib
roslib.load_manifest('rosgui_publisher')

import rosgui.QtBindingHelper #@UnusedImport
from QtCore import Signal, Slot
from QtGui import QAction, QIcon

import PublisherTreeModel
reload(PublisherTreeModel) # force reload to update on changes during runtime
import MessageTreeWidget
reload(MessageTreeWidget)

class PublisherTreeWidget(MessageTreeWidget.MessageTreeWidget):
    remove_publisher = Signal(int)
    publish_once = Signal(int)

    def __init__(self, parent=None):
        super(PublisherTreeWidget, self).__init__(parent)
        self.setModel(PublisherTreeModel.PublisherTreeModel(self))
        self._action_remove_publisher = QAction(QIcon.fromTheme('remove'), 'Remove Selected', self)
        self._action_remove_publisher.triggered.connect(self._handle_action_remove_publisher)
        self._action_publish_once = QAction(QIcon.fromTheme('media-playback-start'), 'Publish Selected Once', self)
        self._action_publish_once.triggered.connect(self._handle_action_publish_once)


    @Slot()
    def remove_selected_publishers(self):
        publisher_ids = self.model().get_publisher_ids(self.selectedIndexes())
        for publisher_id in publisher_ids:
            self.remove_publisher.emit(publisher_id)
        self.model().remove_items_with_parents(self.selectedIndexes())


    def _context_menu_add_actions(self, menu, pos):
        if self.selectionModel().hasSelection():
            menu.addAction(self._action_remove_publisher)
            menu.addAction(self._action_publish_once)
        # let super class add actions
        super(PublisherTreeWidget, self)._context_menu_add_actions(menu, pos)


    def _handle_action_remove_publisher(self, checked):
        self.remove_selected_publishers()


    def _handle_action_publish_once(self, checked):
        for publisher_id in self.model().get_publisher_ids(self.selectedIndexes()):
            self.publish_once.emit(publisher_id)