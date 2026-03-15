from src.camera.CameraStream import CameraStream
from src.controllers.FileController import FileController
import cv2 as cv
import customtkinter as ct


class Controller:
    def __init__(self, file_path):
        self.cam_width = 300
        self.cam_height = 200
        self.cam_index = 0
        self.cam = CameraStream(self.cam_width, self.cam_height, self.cam_index)
        self.fileController = FileController(file_path)
        
        
    def addRow(self, label):
        self.fileController.addNewRow(self.cam.capture(), label)

    def showCam(self):
        return self.cam.capture()

    def showCamTest(self):
        return self.cam.captureTest()
