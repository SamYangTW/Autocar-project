# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-M6_kef63ZW8a5YJvhOGMBDQmLYx_bqv
"""

import cv2
cam = cv2.VideoCapture(0)
while True:
  ret, img = cam.read()
  if img is None:
    break
  vis = img.copy()
  cv2.imshow('getCamera', vis)
  if 0XFF & cv2.waitKey(5) == 27:
    break
cv2.destroyAllWindows()