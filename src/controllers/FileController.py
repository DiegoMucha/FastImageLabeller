import base64 as b64
import pandas as pd
import cv2 as cv
import os

class FileController:
    def __init__(self, file_path):
        self.file_path = file_path

    def createNewFile(self):
        df = pd.DataFrame(columns=["encoded_image, label"])
        df.to_csv(self.file_path)

    def addNewRow(self, image, label):
        new_df = pd.DataFrame({
            "encoded_image": [image],
            "label": [label]
        })
        if not os.path.exists(self.file_path):
            new_df.to_csv(self.file_path, index=False)
        else:
            new_df.to_csv(self.file_path, mode='a', index=False, header=False)