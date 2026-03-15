import cv2 as cv

class CameraStream:
    def __init__(self, width, height, capture_index):
        self.width = width
        self.hegiht = height
        self.cap = cv.VideoCapture(capture_index)

    def capture(self):
        ret, frame = self.cap.read()
        
        if not ret:
            return 0
        
        gray = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        return gray
    
    def captureTest(self):
        ret, frame = self.cap.read()
        
        if not ret:
            return 0
        
        return frame