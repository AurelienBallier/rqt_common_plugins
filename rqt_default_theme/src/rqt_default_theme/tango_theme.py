# Software License Agreement (BSD License)
#
# Copyright (c) 2013, CyclonIT, SASU
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from os import path

import rospkg
import imp

from base_theme import base_theme

class tango_theme(base_theme):
    def __init__(self):
        #Dynamicly load the theme resources
        rp = rospkg.RosPack()
        self.res = imp.load_source('qt_resource_data', path.join(rp.get_path('rqt_default_theme'), 'resource', 'tango_rc.py'))

        self.icons_map = {'media-playback-start' : ':/16/icons/16x16/actions/media-playback-start.png', 
                          'media-playback-pause' : ':/16/icons/16x16/actions/media-playback-pause.png', 
                          'media-playback-stop' : ':/16/icons/16x16/actions/media-playback-stop.png', 
                          'media-skip-backward' : ':/16/icons/16x16/actions/media-skip-backward.png', 
                          'media-skip-forward' : ':/16/icons/16x16/actions/media-skip-forward.png', 
                          'media-seek-backward' : ':/16/icons/16x16/actions/media-seek-backward.png', 
                          'media-seek-forward' : ':/16/icons/16x16/actions/media-seek-forward.png', 
                          'view-refresh' : ':/16/icons/16x16/actions/view-refresh.png', 
                          'zoom-in' : ':/16/icons/16x16/actions/list-add.png', 
                          'zoom-out' : ':/16/icons/16x16/actions/list-remove.png', 
                          'zoom-original' : ':/16/icons/16x16/actions/system-search.png', 
                          'insert-image' : ':/16/icons/16x16/mimetypes/image-x-generic.png', 
                          'image' : ':/16/icons/16x16/mimetypes/image-x-generic.png', 
                          'media-record' : ':/16/icons/16x16/actions/media-record.png', 
                          'document-open' : ':/16/icons/16x16/actions/document-open.png', 
                          'document-save' : ':/16/icons/16x16/actions/document-save.png', 
                          'document-save-as' : ':/16/icons/16x16/actions/document-save-as.png', }
