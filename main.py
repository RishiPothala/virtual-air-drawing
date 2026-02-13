import cv2
import os

# Hide TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from hand_tracker import HandTracker
from drawing import DrawingBoard
from gestures import GestureControl


def main():

    # Open camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera not found")
        return

    # Initialize modules
    tracker = HandTracker()
    board = DrawingBoard()
    gesture = GestureControl()

    print("Air Drawing App Started...")

    while True:

        success, frame = cap.read()

        if not success:
            print("Failed to read camera")
            break

        # Mirror view
        frame = cv2.flip(frame, 1)

        # Detect hand
        frame = tracker.find_hands(frame)

        # Get landmarks
        landmarks = tracker.get_position(frame)

        # If hand detected
        if len(landmarks) != 0:

            x = landmarks[8][1]
            y = landmarks[8][2]

            # Fist → Clear
            if gesture.is_fist(landmarks):

                board.clear()
                board.reset_position()

            # Two fingers → Select color
            elif gesture.is_two_fingers(landmarks):

                    board.reset_position()

                    if y < 90:   # Toolbar height

                        # Green
                        if 10 < x < 80:
                            board.set_color((0,255,0))

                        # Red
                        elif 90 < x < 160:
                            board.set_color((0,0,255))

                        # Blue
                        elif 170 < x < 240:
                            board.set_color((255,0,0))

                        # Yellow
                        elif 250 < x < 320:
                            board.set_color((0,255,255))

                        # Eraser
                        elif 340 < x < 410:
                            board.set_color((0,0,0))

                        # Clear
                        elif 430 < x < 500:
                            board.clear()

                        # Save
                        elif 530 < x < 600:
                            cv2.imwrite("drawing.png", board.canvas)
                            print("Saved drawing.png")

            # One finger → Draw
            elif gesture.is_index_up(landmarks):

                board.draw(x, y)

            else:
                board.reset_position()

        # Draw color palette
        frame = board.draw_toolbar(frame, board.active_color)

        # Merge drawing with camera
        frame = board.merge(frame)

        # Show output
        cv2.imshow("Virtual Air Drawing", frame)

        # Exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    print("App Closed")


if __name__ == "__main__":
    main()
