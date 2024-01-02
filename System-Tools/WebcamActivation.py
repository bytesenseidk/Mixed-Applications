import cv2
import numpy as np

def webcam_activation():
    camera = cv2.VideoCapture(0) # Camera selection
    while True:
        # Camera validation & Camera activation
        val, frame = camera.read()
        # Show picture or video  
        cv2.imshow("frame", frame)
        # Exit by pressing 'e'
        if cv2.waitKey(1) == ord("e"):
            break

if __name__ == "__main__":
    webcam_activation()

