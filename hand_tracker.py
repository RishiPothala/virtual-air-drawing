import cv2
import mediapipe as mp


class HandTracker:

    def __init__(self, detection_conf=0.8, track_conf=0.8):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=detection_conf,
            min_tracking_confidence=track_conf
        )

        self.mp_draw = mp.solutions.drawing_utils


    def find_hands(self, frame, draw=True):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.result = self.hands.process(rgb)

        if self.result.multi_hand_landmarks:

            for hand in self.result.multi_hand_landmarks:

                if draw:
                    self.mp_draw.draw_landmarks(
                        frame,
                        hand,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return frame


    def get_position(self, frame, hand_no=0):

        landmark_list = []

        if self.result.multi_hand_landmarks:

            hand = self.result.multi_hand_landmarks[hand_no]

            for id, lm in enumerate(hand.landmark):

                h, w, _ = frame.shape

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                landmark_list.append([id, cx, cy])

        return landmark_list
