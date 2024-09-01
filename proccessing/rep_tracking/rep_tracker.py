from .rep import Rep

class RepTracker:
    def __init__(self):
        # Should hold objects of type Rep
        self.past_dir = "Standing"
        self.reps = []
    
    def is_rep_complete(self, is_standing: bool):
        if is_standing and (self.past_dir != "Standing"):
            return True
        else:
            return False
            