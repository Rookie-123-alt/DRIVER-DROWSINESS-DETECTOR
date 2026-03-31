import cv2
from detector import FaceDetector
from utils import eye_aspect_ratio, mouth_aspect_ratio
from alert import trigger_alert

EYE_THRESH = 0.25
EYE_FRAMES = 20
YAWN_THRESH = 0.7

counter = 0

detector = FaceDetector()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    points = detector.get_landmarks(frame)

    if points:
        left_eye = [points[i] for i in [33,160,158,133,153,144]]
        right_eye = [points[i] for i in [362,385,387,263,373,380]]
        mouth = [points[i] for i in [61,291,81,178,13,14,311,402,308]]

        ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2
        mar = mouth_aspect_ratio(mouth)

        if ear < EYE_THRESH:
            counter += 1
            if counter >= EYE_FRAMES:
                trigger_alert()
        else:
            counter = 0

        if mar > YAWN_THRESH:
            trigger_alert()

        cv2.putText(frame, f"EAR: {ear:.2f}", (30, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
