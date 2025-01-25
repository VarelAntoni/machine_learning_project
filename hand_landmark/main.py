from hand_detection import HandDetection
import cv2

handDetection = HandDetection(min_detection_confidence=0.5, min_tracking_confidence=0.5)

webcam = cv2.VideoCapture()
webcam.open(0, cv2.CAP_DSHOW)

while True:
    status, frame = webcam.read()
    frame = cv2.flip(frame, 1)
    handLandmarks = handDetection.findHandLandmarks(image=frame, draw = True)


    cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) == ord('Q'):
        break
cv2.destroyAllWindows()
webcam.release()
