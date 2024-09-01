import numpy as np
from time_tracker import TimeTracker
from rep_tracking.rep_tracker import RepTracker

# Goal of this motion tracker is to figure out if
# The squat is in the top, eccentric, bottom, or concentric
class MotionTracker:
    
    def __init__(self, time_tracker : TimeTracker, rep_tracker : RepTracker):
        # This will be set to the landmark where the hip is lowest
        self.lowest_y_value = 0
        self.lowest_point = []
        self.dir = "Standing"
        self.time_tracker = time_tracker
        self.rep_tracker = rep_tracker
        self.is_standing = True
    
    def direction_motion(self, landmarks_list):
        self.is_standing = self.is_standing_met(landmarks_list)
        # HAS TO BE HERE OTHERWISE WON'T WORK
        self.time_tracker.track_total_time(self.is_standing, self.dir)

            
        
        if self.is_standing:
            self.dir = "Standing"
        else:
            self.dir = self.moving_motion(landmarks_list)
        

        return self.dir
        
    def calculate_angle(self, first:list, mid:list, end:list):
        first = np.array(first)
        mid = np.array(mid)
        end = np.array(end)
        
        rad = np.arctan2(first[1] - mid[1], first[0] - mid[0]) - np.arctan2(end[1] - mid[1], end[0] - mid[0])  
        deg = np.abs(rad*180.0/np.pi)
        
        if deg > 180.0:
            deg = 360.0 - deg
        
        return deg
    
    def is_standing_met(self, landmarks_list):
        length = len(landmarks_list)
        
        try:
            last_landmark = landmarks_list[length - 1]
            left_hip = [last_landmark[23].x, last_landmark[23].y]
            left_knee = [last_landmark[25].x, last_landmark[25].y]
            left_ankle = [last_landmark[27].x, last_landmark[27].y]

            left_leg_angle = self.calculate_angle(left_hip, left_knee, left_ankle)
            
            right_hip = [last_landmark[24].x, last_landmark[24].y]
            right_knee = [last_landmark[26].x, last_landmark[26].y]
            right_ankle = [last_landmark[28].x, last_landmark[28].y]
            
            right_leg_angle = self.calculate_angle(right_hip, right_knee, right_ankle)
            
            if (left_leg_angle + right_leg_angle) / 2.0 > 172:
                return True
            else:
                return False
        except:
            return True

    def moving_motion(self, landmarks_list):
        # This is the average y-value of the hips
        # At the first 3 landmarks
        try:
            first_y_value = 0
            length = len(landmarks_list)
            
            for i in range(int(length / 2)):
                average_hip = (landmarks_list[i][23].y + landmarks_list[i][24].y) / 2.0
                first_y_value += average_hip
            
            first_y_value /= length / 2
            
            last_y_value = 0
            
            for i in range(int(length / 2), length):
                average_hip = (landmarks_list[i][23].y + landmarks_list[i][24].y) / 2.0
                last_y_value += average_hip
                
            last_y_value /= length / 2
            
            if last_y_value > self.lowest_y_value:
                self.lowest_y_value = last_y_value
                self.lowest_point = landmarks_list[length - 1]

            
            dif = last_y_value - first_y_value
            
            if dif >= 0:
                return "Down"
            else:
                if self.dir == "Down":
                    self.time_tracker.track_eccentric_time()
                return "Up"
        except:
            pass
    
    def clear(self):
        self.lowest_point = []

            
        
