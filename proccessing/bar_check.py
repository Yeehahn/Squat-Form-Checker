class BarCheck:
    def __init__(self):
        self.start_z = None
        self.bar_allignment_value = 0
    
    def check_bar_allignment(self, landmarks):
        try:
            avg_z = (landmarks[12].z + landmarks[11].z) / 2
            if (self.start_z == None) or self.bar_allignment_value < -10:
                self.start_z = avg_z
            else:
                if abs(abs(avg_z) - abs(self.start_z)) > 0.07:
                    self.bar_allignment_value -= 2
                else:
                    self.bar_allignment_value += 1
        except:
            pass
        
    def clear(self):
        self.start_z = None
        self.bar_allignment_value = 0