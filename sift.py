#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:44:01 2022

@author: cytech
"""
import cv2

img = cv2.imread('monkey.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp, des = sift.detectAndCompute(gray_img, None)

kp_img = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow('SIFT', kp_img)
cv2.waitKey()