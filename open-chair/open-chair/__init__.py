# Copyright 2017 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
import time

from subprocess import Popen, PIPE

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Tiago Chiaveri da Costa'

LOGGER = getLogger(__name__)
CWD_PATH = os.path.dirname(__file__)


class HeartMonitor(MycroftSkill):
    def __init__(self):
        super(HeartMonitor, self).__init__(name="HeartMonitor")

    def initialize(self):
        what_my_heart_rate = IntentBuilder("HeartMonitor"). \
            require("HeartMonitor").build()
        self.register_intent(what_my_heart_rate, self.handle_what_my_heart_rate)

    def handle_what_my_heart_rate(self, message)
        cmd = "uhubctl -a off -p 1  -l 1-1 -r 100"
        cmd1 = "uhubctl -a on -p 1  -l 1-1 -r 100"
        '''
        self.speak("Turning off the mouse... Soon it will be used to activate the motor of the wheelchair")
        os.popen(cmd,)
        self.speak("The mouse will be disabled for 5 seconds.")
        self.speak("Turning on the mouse")
        os.popen(cmd1,)
        '''
        self.speak('The command occurred correctly.')
    def stop(self):
        pass


def create_skill():
    return HeartMonitor()
