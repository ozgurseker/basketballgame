#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 03:48:53 2023

@author: ozgurseker
"""

import numpy as np
import matplotlib.pyplot as plt
import ipympl
import imageio.v3 as iio
# import skimage

image = iio.imread(uri="halfcourtimage.PNG")
print(image.shape)
print(image)

imagematrix = np.zeros(image.shape[0:2])


for c in range(4):
    imagematrix = imagematrix + image[:,:,c]
    
# Pixels of the lines for half-court. 
y_s, x_s = np.where(imagematrix != 1020)


# To locate 3pt area:
# For same x values, it must have second highest y (after lower border)

borders_x = [np.min(x_s), np.max(x_s)]
borders_y = [np.min(y_s), np.max(y_s)]


# Next steps
# Locate the basket
# 3pt-finder function 