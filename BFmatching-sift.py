#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  7 13:28:00 2022

@author: cytech
"""
import cv2

img1 = cv2.imread('p (1).jpg', 0)
img2 = cv2.imread('new p (1).png', 0)


sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)


# matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)# draw first 50 matches
match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)
cv2.imshow('Matches', match_img)
cv2.waitKey()