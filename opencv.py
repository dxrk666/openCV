# -*- coding: utf-8 -*-
"""openCV.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18OaGTftpSZcgXYsqW_dYjLrl1R1qutHN
"""

!pip install opencv-python

import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('image1.jpg')

cv2_imshow(image)

cv2.waitKey(0)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('oq-qora.jpg', gray_image)
print("Oq-qora rasm saqlandi")