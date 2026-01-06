import cv2
import numpy as np
import os

class MotionDetector:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # Background subtractor MOG2
        self.fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=False)

    def run(self):
        if not self.cap.isOpened():
            print("Error: Webcam not found.")
            return

        print("Motion Detector Started. Press 'q' to quit.")
        print("Waiting for motion...")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Apply Background Subtraction
            fgmask = self.fgbg.apply(frame)

            # Remove noise (Erosion & Dilation)
            kernel = np.ones((5,5), np.uint8)
            fgmask = cv2.erode(fgmask, kernel, iterations=1)
            fgmask = cv2.dilate(fgmask, kernel, iterations=2)

            # Find Contours
            contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            motion_detected = False
            for contour in contours:
                # Filter small movements
                if cv2.contourArea(contour) < 500:
                    continue
                
                motion_detected = True
                # Draw bounding box
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

            # Status Text
            status = "Motion Detected!" if motion_detected else "Idle"
            color = (0, 0, 255) if motion_detected else (0, 255, 0)
            cv2.putText(frame, f"Status: {status}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            # Show Frame
            cv2.imshow('Security Feed', frame)
            # cv2.imshow('Mask', fgmask) # Uncomment to see the mask

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

def main():
    detector = MotionDetector()
    detector.run()

if __name__ == "__main__":
    main()
