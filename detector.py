import cv2
import mediapipe as mp
from scipy.spatial import distance
import pygame

# ---------------- AUDIO SETUP ----------------
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.mixer.music.load("static/alarm.mp3")
pygame.mixer.music.set_volume(1.0)

# ---------------- MEDIAPIPE SETUP ----------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# ---------------- PARAMETERS ----------------
EAR_THRESHOLD = 0.20
FRAME_CHECK = 10   # lower for faster detection

counter = 0

# ---------------- EAR FUNCTION ----------------
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# ---------------- MAIN GENERATOR ----------------
def generate_frames():
    global counter
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        h, w = frame.shape[:2]
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        ear = 0
        status = "Awake"

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                left_eye = []
                right_eye = []

                # LEFT EYE
                for idx in LEFT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    left_eye.append((x, y))

                # RIGHT EYE
                for idx in RIGHT_EYE:
                    x = int(face_landmarks.landmark[idx].x * w)
                    y = int(face_landmarks.landmark[idx].y * h)
                    right_eye.append((x, y))

                # EAR Calculation
                ear_left = eye_aspect_ratio(left_eye)
                ear_right = eye_aspect_ratio(right_eye)
                ear = (ear_left + ear_right) / 2.0

                # ---------------- CORE LOGIC ----------------
                if ear < EAR_THRESHOLD:
                    counter += 1
                else:
                    counter = 0

                if counter >= FRAME_CHECK:
                    status = "DROWSY"
                else:
                    status = "Awake"

                # ---------------- SOUND CONTROL ----------------
                if status == "DROWSY":
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play(loops=-1)
                else:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()

                # ---------------- DISPLAY ----------------
                cv2.putText(frame, f"EAR: {round(ear, 2)}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                cv2.putText(frame, f"Counter: {counter}", (10, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

                color = (0, 255, 0) if status == "Awake" else (0, 0, 255)

                cv2.putText(frame, status, (10, 70),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 3)

                # Red alert border
                if status == "DROWSY":
                    cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 10)

        # ---------------- STREAM FRAME ----------------
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')