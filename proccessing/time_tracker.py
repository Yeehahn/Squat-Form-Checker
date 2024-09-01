import time

class TimeTracker:
    def __init__ (self):
        self.rep_time = None
        self.start_time = None
        self.eccentric_time = None
        self.cur_timestamp = None
        
    def track_total_time(self, is_standing : bool, dir : str):
        if is_standing and (dir != "Standing"):
            self.rep_time = self.cur_timestamp - self.start_time
        elif not is_standing and (dir == "Standing"):
            self.start_time = self.cur_timestamp
            
    def track_eccentric_time(self):
        self.eccentric_time = self.cur_timestamp - self.start_time
        
    def set_current_time(self, timestamp):
        self.cur_timestamp = timestamp
        
    def clear(self):
        self.rep_time = 0
        self.start_time = 0
        self.eccentric_time = 0
        self.cur_timestamp = 0
        
