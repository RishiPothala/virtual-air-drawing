class GestureControl:

    def is_index_up(self, landmarks):

        if len(landmarks) < 9:
            return False

        tip = landmarks[8][2]
        lower = landmarks[6][2]

        return tip < lower


    def is_middle_up(self, landmarks):

        if len(landmarks) < 13:
            return False

        tip = landmarks[12][2]
        lower = landmarks[10][2]

        return tip < lower


    def is_two_fingers(self, landmarks):

        return self.is_index_up(landmarks) and self.is_middle_up(landmarks)


    def is_fist(self, landmarks):

        if len(landmarks) < 21:
            return False

        fingers = [8, 12, 16, 20]

        for tip in fingers:
            if landmarks[tip][2] < landmarks[tip - 2][2]:
                return False

        return True
