import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

class FaceDetector:
    def __init__(self):
        self.mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

    def get_landmarks(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.mesh.process(rgb)

        if result.multi_face_landmarks:
            face = result.multi_face_landmarks[0]
            h, w, _ = frame.shape
            return [(int(lm.x * w), int(lm.y * h)) for lm in face.landmark]
        return None
