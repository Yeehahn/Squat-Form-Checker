class Rep:
    def __init__(self, lowest_landmark, knee_path, bar_path, ecc_time, total_time):
        self.is_good_depth = self.check_depth(lowest_landmark)
        self.is_good_knee_path = self.check_knee_path(knee_path)
        self.is_good_bar_allignment = self.check_bar_allignment(bar_path)
        self.is_good_ecc_time = self.check_ecc_time(ecc_time)
        self.total_time = total_time
    
    def check_depth(self, lowest_landmark):
        avg_hip = (lowest_landmark[23].y + lowest_landmark[24].y) / 2
        avg_knee = (lowest_landmark[25].y + lowest_landmark[26].y) / 2
        if avg_hip - avg_knee < 0.0:
            return True
        else:
            return False
      
    def check_knee_path(self, knee_path):
        if knee_path > 10:
            return True
        else:
            return False
        
    def check_ecc_time(self, ecc_time):
        if ecc_time > 0.9:
            return True
        else:
            return False
        
    def check_bar_allignment(self, bar_path):
        if bar_path > 10:
            return True
        else:
            return False
        
    def __str__(self):
        return (
            f"Rep Summary:\n"
            f"  Good Depth: {self.is_good_depth}\n"
            f"  Good Knee Path: {self.is_good_knee_path}\n"
            f"  Good Bar Alignment: {self.is_good_bar_allignment}\n"
            f"  Good Eccentric Time: {self.is_good_ecc_time}\n"
            f"  Total Time: {self.total_time} seconds"
        )