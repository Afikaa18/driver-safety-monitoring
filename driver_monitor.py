from scipy.spatial import distance
from pygame import mixer
import cv2

# 1. Initialising Audio Alert
mixer.init()
mixer.music.load("c:/Users/user/Downloads/music.wav") #path of music file

# 2. Load OpenCV’s built-in Face and Eye Detectors (Already Included)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')

# Threshold Configuration
# As OpenCV detects whether eyes are open or closed based on object detection,
# if the eyes are closed, “eye_cascade” will not detect the presence of eyes.
frame_check = 5  # The number of eye frames was not detected before the alarm sounded
flag = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
        
    frame = cv2.flip(frame, 1) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Face Detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))
    
    # Initial state in each frame (assuming the eyes are closed until proven otherwise)
    eyes_detected = False
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Box face
        
        # The area of the face where the eyes are located (Region of Interest)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # Eye detection within the face area
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(30, 30))
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2) # Green Box (Hijau)
            
        if len(eyes) >= 1:
            eyes_detected = True

    # Count Sleepy Frames
    if len(faces) > 0: # Only count if there is a face in the camera
        if not eyes_detected:
            flag += 1
            print(f"Eyes Closed/Not Detected: {flag}")
            if flag >= frame_check:
                cv2.putText(frame, "                       WARNING!               ", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "                       WARNING!               ", (10, frame.shape[0] - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                if not mixer.music.get_busy():
                    mixer.music.play()
        else:
            flag = 0
            mixer.music.stop() # Turn off the music if your eyes open again
            
    cv2.imshow("Drowsiness Detection (OpenCV Stable Version)", frame)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()