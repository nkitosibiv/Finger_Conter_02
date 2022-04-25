import cv2
import mediapipe as mp
import time

 
class handdetector():
    def __init__(self, mode=False, maxHands=2,  complexity=1, detection=0.75, trackCon=0.75):
        self.Hands = mp.solutions.hands
        self.hands = self.Hands.Hands( mode,  maxHands,  complexity, detection, trackCon)
        self.mpDraw = mp.solutions.drawing_utils  # утилита для рисования
        self.fingertips = [4, 8, 12, 16, 20]
    
    def findHands(self, img, darw=True):
        image = cv2.flip(img, 1)
        RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(RGB_image)
        if draw:

            for handlms in self.result.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpDraw.HAND_CONNECTIONS)