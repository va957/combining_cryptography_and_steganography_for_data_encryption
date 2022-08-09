import cv2
import numpy as np
import math
def mse(img1,img2):
     mse = np.mean((img1 - img2) ** 2 )
     a=mse
     return a
 
def psnr1(img1, img2):
   mse = np.mean((img1 - img2) ** 2 )
   if mse < 1.0e-10:
      return 100
   return 10 * math.log10(255.0**2/mse)
gt = cv2.imread(r"D:\SEMESTER 2\CAPSTONE\FINAL\IMAGES\3.png")
img= cv2.imread(r"D:\SEMESTER 2\CAPSTONE\FINAL\IMAGES\3stego.png")
 
print("The PSNR Value is" ,psnr1(gt,img))
print("The MSE Value is" ,mse(gt,img))

import matplotlib.pyplot as plt
import cv2
im = cv2.imread(r"D:\SEMESTER 2\CAPSTONE\FINAL\IMAGES\3.png")
vals = im.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)

im1 = cv2.imread(r"D:\SEMESTER 2\CAPSTONE\FINAL\IMAGES\3stego.png")
vals = im1.mean(axis=2).flatten()
# plot histogram with 255 bins
b, bins, patches = plt.hist(vals, 255)

plt.xlim([0,255])
plt.show()

