from cv2 import imshow
from cv2 import waitKey
from PIL import Image
import time
import pandas as pd

df = pd.read_csv("hello.csv")
print(df.head(20))
print(type(df["encoded_image"].iloc[0]))
