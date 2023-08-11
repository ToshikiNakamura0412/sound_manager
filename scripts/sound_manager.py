#!/usr/bin/python3

import subprocess

import rospy
from std_msgs.msg import Bool, Int32

class SoundManager:
    def __init__(self):
        rospy.init_node('sound_manager')
        print('=== sound manager ===')

        # get param
        self.ANNOUNCE_SOUND_PATH = rospy.get_param('~ANNOUNCE_SOUND_PATH', "../sounds/announcement_short.wav")
        self.is_sound = rospy.get_param('~is_sound', True)
        self.volume = rospy.get_param("~volume", 50)

    def process(self):
        self.set_volume()
        r = rospy.Rate(0.5)
        while not rospy.is_shutdown():
            self.sound_once()
            r.sleep()

    def set_volume(self):
        volume_cmd = "amixer sset Master " + str(self.volume) + "%"
        subprocess.call(volume_cmd.split())

    def sound_once(self):
        if self.is_sound == True :
            announce_cmd = "aplay " + self.ANNOUNCE_SOUND_PATH
            subprocess.call(announce_cmd.split())

if __name__ == '__main__':
    sound_manager = SoundManager()
    sound_manager.process()
