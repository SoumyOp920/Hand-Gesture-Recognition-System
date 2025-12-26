# -------- Importing Libraries --------
import time
import cv2
import mediapipe as mp

# -------- MediaPipe Setup --------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# -------- Webcam --------
cap = cv2.VideoCapture(0)

# -------- FPS --------
prev_Time = 0

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame, 1)  # Mirror fix

    # -------- FPS Calculation --------
    current_Time = time.time()
    fps = 1 / (current_Time - prev_Time) if prev_Time != 0 else 0
    prev_Time = current_Time

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):

            # -------- Hand Label (Left / Right) --------
            hand_label = result.multi_handedness[idx].classification[0].label

            fingers = []

            # -------- Fingers & Thumb --------
            fingers.append(hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x)    #Thumb
            fingers.append(hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y)    # Index
            fingers.append(hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y)  # Middle
            fingers.append(hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y)  # Ring
            fingers.append(hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y)  # Pinky

            finger_count = fingers.count(True)

            # -------- Gesture Logic --------
            if finger_count == 0:
                gesture = "FIST"
            elif finger_count == 1 and fingers[1]:
                gesture = "ONE"
            elif finger_count == 2 and fingers[1] and fingers[2]:
                gesture = "TWO"
            elif finger_count == 3 and fingers[1] and fingers[2] and fingers[3]:
                gesture = "THREE"
            elif finger_count == 4 and not fingers[0]:
                gesture = "FOUR"
            elif finger_count == 5:
                gesture = "OPEN PALM"
            elif fingers[0] and not any(fingers[1:]):
                gesture = "THUMBS UP"
            elif finger_count == 2 and fingers[1] and fingers[4]:
                gesture = "YOO!"
            elif finger_count == 2 and fingers[0] and fingers[1]:
                gesture = "LOVE!"
            elif finger_count == 1 and fingers[4]:
                gesture = "PEE!"
            else:
                gesture = "GESTURE"

            # -------- Display Gesture --------
            cv2.putText(
                frame,
                f"{gesture} ({finger_count})",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # -------- Display FPS --------
            cv2.putText(
                frame,
                f"FPS: {int(fps)}",
                (520, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (255, 0, 0),
                2
            )

            # -------- Display Hand Label --------
            cv2.putText(
                frame,
                f"Hand: {hand_label}",
                (20, 90),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            # -------- Draw Landmarks --------
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow("Hand Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
