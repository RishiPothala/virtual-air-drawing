import cv2
import numpy as np


class DrawingBoard:

    def __init__(self, width=640, height=480):

        self.width = width
        self.height = height

        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)

        self.prev_x = None
        self.prev_y = None

        # Smoothed position
        self.smooth_x = None
        self.smooth_y = None

        self.color = (0, 255, 0)
        self.active_color = self.color
        self.brush = 5

        # Smoothing factor (0.1 = more smooth, 0.5 = faster)
        self.alpha = 0.25
    

    def draw(self, x, y):

        # First point
        if self.smooth_x is None:
            self.smooth_x = x
            self.smooth_y = y

        # Apply smoothing (Exponential Moving Average)
        self.smooth_x = int(self.alpha * x + (1 - self.alpha) * self.smooth_x)
        self.smooth_y = int(self.alpha * y + (1 - self.alpha) * self.smooth_y)

        if self.prev_x is None:
            self.prev_x = self.smooth_x
            self.prev_y = self.smooth_y

        cv2.line(
            self.canvas,
            (self.prev_x, self.prev_y),
            (self.smooth_x, self.smooth_y),
            self.color,
            self.brush
        )

        self.prev_x = self.smooth_x
        self.prev_y = self.smooth_y


    def reset_position(self):

        self.prev_x = None
        self.prev_y = None
        self.smooth_x = None
        self.smooth_y = None


    def clear(self):

        self.canvas = np.zeros(
            (self.height, self.width, 3),
            dtype=np.uint8
        )

        self.reset_position()


    def merge(self, frame):

        return cv2.add(frame, self.canvas)



    def draw_toolbar(self, frame, active_color):

        # Toolbar background
        cv2.rectangle(frame, (0, 0), (640, 90), (40, 40, 40), -1)

        buttons = [
            {"name": "GREEN",  "color": (0,255,0),   "x": 10},
            {"name": "RED",    "color": (0,0,255),   "x": 90},
            {"name": "BLUE",   "color": (255,0,0),   "x": 170},
            {"name": "YELLOW", "color": (0,255,255), "x": 250},
            {"name": "ERASER", "color": (0,0,0),     "x": 340},
            {"name": "CLEAR",  "color": None,        "x": 430},
            {"name": "SAVE",   "color": None,        "x": 530}
        ]

        for btn in buttons:

            x1 = btn["x"]
            y1 = 10
            x2 = x1 + 70
            y2 = 70

            # Highlight active color
            if btn["color"] == active_color:
                cv2.rectangle(frame, (x1-3,y1-3),(x2+3,y2+3),(255,255,255),2)

            # Button background
            cv2.rectangle(frame,(x1,y1),(x2,y2),(70,70,70),-1)

            # Color circle
            if btn["color"] is not None:
                cv2.circle(frame,(x1+35,y1+30),15,btn["color"],-1)

            # Text
            cv2.putText(
                frame,
                btn["name"],
                (x1+5,y1+60),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (255,255,255),
                1
            )

        return frame


    def set_color(self, color):
        self.color = color
        self.active_color = color

