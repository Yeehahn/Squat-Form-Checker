import mediapipe as mp

    
    # Finds all of the land marks from the image
    # Stores the landmarks into the landmarks list
    # Maintains the lists size to a maximum of 5
    # Returns the landmark
def find_landmarks(image, landmarks_list : list):
    mp_pose = mp.solutions.pose
    with mp_pose.Pose() as pose:
        results = pose.process(image)
        try:
            landmarks = results.pose_landmarks.landmark
            landmarks_list.append(landmarks)
        except:
            pass
        
        while len(landmarks_list) > 8:
            landmarks_list.pop(0)
        
        return results

                
    
        
        
        