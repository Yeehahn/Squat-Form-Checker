
import cv2
import mediapipe as mp
from formcheck import FormCheck 


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

form_check = FormCheck()

cap = cv2.VideoCapture("videos\Jeremy Squat.mp4")

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        # Set color properly
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        results = form_check.next_image(image, timestamp)
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        cv2.putText(image, form_check.get_dir(), (40,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (256,256,256), 1, cv2.LINE_AA)
        
        cv2.imshow("Mediapipe Feed", image)
        
        

        if (cv2.waitKey(10) & 0xFF == ord("q")):
            break
        
        
    reps_list = form_check.rep_tracker.reps
    for rep in reps_list:
        print(rep)