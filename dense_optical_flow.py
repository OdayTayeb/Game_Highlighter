# -*- coding: utf-8 -*-
"""Dense Optical Flow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jiGPB-Lo3UsyKi3TLZrNpiFALqFpXt_n
"""

# from google.colab import drive

# drive.mount('/content/gdrive/')

import numpy as np
import cv2

def calculate_movement(bgr):
  gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
  black = np.count_nonzero(gray==0)
  H = bgr.shape[0]
  W = bgr.shape[1]
  colored = H*W - black
  return colored/(H*W)

def amount_of_movement(videoURL,skip):
  result = []
  result.append(0)
  cap = cv2.VideoCapture(videoURL)
  if (cap.isOpened()== False): 
    print("Error opening video stream or file")
  frameNumber = 1
  totalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  ret, frame1 = cap.read()
  prvs = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
  hsv = np.zeros_like(frame1)
  hsv[..., 1] = 255
  while(cap.isOpened()):
    ret, frame2 = cap.read()
    frameNumber += 1
    aom=0
    #print(frameNumber)
    if ret == True:
      if frameNumber % skip == 2 or frameNumber == totalFrames:
        next = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang*180/np.pi/2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        aom = calculate_movement(bgr)
        result.append(aom)
      else:
        result.append(aom)
    else:
      break
    prvs = next  
  cap.release()
  cv2.destroyAllWindows()
  return result

