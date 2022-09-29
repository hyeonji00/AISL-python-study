import numpy as np
from PIL import Image # 이미지 사용
import cv2 # 이미지 resize

import matplotlib.pyplot as plt # matlab

path = "test/object_detection/cat_dog.jpeg"

image = Image.open(path) # 이미지 불러오기
image.show() # 이미지 띄우기

# img = np.array(image)
# print(img.shape)

# 이미지 resize
# resize_img = cv2.resize(img, (275, 183))
# print(resize_img.shape)

# 이미지 출력
# plt.imshow(resize_img)
# plt.show()