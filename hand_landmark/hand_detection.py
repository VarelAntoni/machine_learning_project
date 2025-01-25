import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

class HandDetection:
    def __init__(self, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.hands = mpHands.Hands(max_num_hands=max_num_hands, min_detection_confidence=min_detection_confidence,
                                    min_tracking_confidence=min_tracking_confidence)
       
    def findHandLandmarks(self, image, handNumber=0, draw = False):
            originalImage = image
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image)

            allLandmarkLists = []

            if results.multi_hand_landmarks:
                for hand in results.multi_hand_landmarks:  
                    landmarkList = []  
                    for id, landmark in enumerate(hand.landmark):
                        imgH, imgW, imgC = originalImage.shape
                        xPos, yPos = int(landmark.x * imgW), int(landmark.y * imgH)
                        landmarkList.append([id, xPos, yPos]) 
                    allLandmarkLists.append(landmarkList)  
                    if draw:
                        mpDraw.draw_landmarks(originalImage, hand, mpHands.HAND_CONNECTIONS)

            return allLandmarkLists


