class KneeCheck:
    def __init__(self):
        self.knee_value = 0
        
    def check_knee_path(self, landmark_list : list):
        length = len(landmark_list)

        f_left_knee = [0, 0]
        f_right_knee = [0, 0]
        for i in range(int(length / 2)):
            f_left_knee[0] += landmark_list[i][25].x 
            f_left_knee[1] += landmark_list[i][25].z 
            f_right_knee[0] += landmark_list[i][26].x 
            
        e_left_knee = [0, 0]
        e_right_knee = [0, 0]
        
        for i in range(int(length / 2), length):
            e_left_knee[0] += landmark_list[i][25].x 
            e_left_knee[1] += landmark_list[i][25].z 
            e_right_knee[0] += landmark_list[i][26].x 
            e_right_knee[1] += landmark_list[i][26].z 
        
        left_knee_path = (e_left_knee[0] - f_left_knee[0]) / (e_left_knee[1] - f_left_knee[1])
        right_knee_path = (e_right_knee[0] - f_right_knee[0]) / (e_right_knee[1] - f_right_knee[1])
        feet_path = self.find_feet_path(landmark_list)
        
        if abs(abs(feet_path[0]) - abs(left_knee_path)) > 0.07:
            self.knee_value -= 2
        else:
            self.knee_value += 1
            
        if abs(abs(feet_path[1]) - abs(right_knee_path)) > 0.07:
            self.knee_value -= 2
        else:
            self.knee_value += 1
            
    
    # This theoretically should slow down the program by al ot
    # And theoretically I should be able to just check the last index
    # But for whatever reason I can't
    # So this is going to have to do until I find a better solution
    def find_feet_path(self, landmark_list):
        left_foot_heel = [0,0]
        left_foot_index = [0,0]
        right_foot_heel = [0,0]
        right_foot_index = [0,0]
        
        # W CODING HOORAH
        for i in range(len(landmark_list)):
            left_foot_heel[0] += landmark_list[i][29].x
            left_foot_heel[1] += landmark_list[i][29].z
            left_foot_index[0] += landmark_list[i][31].x
            left_foot_index[1] += landmark_list[i][31].z
            right_foot_heel[0] += landmark_list[i][30].x
            right_foot_heel[1] += landmark_list[i][30].z
            right_foot_index[0] += landmark_list[i][32].x
            right_foot_index[1] += landmark_list[i][32].z
        
        # Index 0 is left foot, index 1 is right ofot
        feet_path = [0, 0]
        feet_path[0] = (left_foot_index[0] - left_foot_heel[0]) / (left_foot_index[1] - left_foot_heel[0])
        feet_path[1] = (right_foot_index[0] - right_foot_heel[0]) / (right_foot_index[1] - right_foot_heel[0])
        
        return feet_path
            
    def clear(self):
        self.knee_value = 0