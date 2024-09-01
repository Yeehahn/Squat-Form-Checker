import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import landmark_finder
from motion_tracker import MotionTracker 
from rep_tracking.rep import Rep
from rep_tracking.rep_tracker import RepTracker
from time_tracker import TimeTracker
from knee_check import KneeCheck
from bar_check import BarCheck


import time
class FormCheck:
    def __init__(self):
        self.rep_tracker = RepTracker()
        self.time_tracker = TimeTracker()
        self.knee_check = KneeCheck()
        self.bar_check = BarCheck()
        # Inject time_tracker in so that formcheck can access time cleanly
        self.motion_tracker = MotionTracker(self.time_tracker, self.rep_tracker)
        # List's max size should be 4
        self.landmark_list = []
        
    def next_image(self, image, timestamp):
        self.time_tracker.set_current_time(timestamp)
        
        results = landmark_finder.find_landmarks(image, self.landmark_list)
        self.rep_tracker.past_dir = self.motion_tracker.dir
        self.motion_tracker.direction_motion(self.landmark_list)

        if not self.motion_tracker.is_standing:
            self.knee_check.check_knee_path(self.landmark_list)
            self.bar_check.check_bar_allignment
        
        
        # TESTING
        if self.rep_tracker.is_rep_complete(self.motion_tracker.is_standing):
            self.rep_tracker.reps.append(Rep(self.motion_tracker.lowest_point, self.knee_check.knee_value, self.bar_check.bar_allignment_value, self.time_tracker.eccentric_time, self.time_tracker.rep_time))
            self.clear()
               
        return results
    
    def get_dir(self):
        return self.motion_tracker.dir
    
    def get_reps(self):
        return len(self.rep_tracker.reps)
    
    def clear(self):
        self.motion_tracker.clear()
        self.knee_check.clear()
        self.bar_check.clear()
        self.time_tracker.clear()
        
        