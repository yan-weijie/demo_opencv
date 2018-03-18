#coding : utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import unittest, time, re, random,os
import cv2 
from math import *
import numpy as np
import matplotlib.pyplot as plt
path=os.path.abspath(".")    
imagepath=path+"\\pic\\test\\"
image = cv2.imread(imagepath+"image.png")
height, width = image.shape[:2]
start_row, start_col = int(0), int(0)
end_row, end_col = int(height/4), int(width/5)
cropped = image[start_row:int(end_row) , start_col:int(end_col)]
sh,sw=cropped.shape[:2]
matchrate=0
totalrate=0
def match_img(Target):
    global matchrate,totalrate
    print Target
    img_rgb = cv2.imread(imagepath+"image3.png")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.97
    matchrate = 0.05
    loc=[]
    loc = np.where( res >= threshold)
    while (len(loc[0])==0):        
        loc = np.where( res >= threshold)        
        threshold+= -0.2 
        matchrate+= -0.01
        if matchrate<0.01:
            return False          
    totalrate=totalrate+matchrate
    try:                   
     for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,30,255), 4)
        cv2.putText(img_rgb, "Matchrate: %s%%"%(threshold*100), (500,400),cv2.FONT_HERSHEY_COMPLEX, 1, (0,120,220), 2, 8,0)
        cv2.putText(img_rgb, "Total: %s%%"%(totalrate*100), (500,450),cv2.FONT_HERSHEY_COMPLEX, 1, (0,20,200), 2, 8,0)
     cv2.imshow('UI AUTO',img_rgb)
     cv2.waitKey(1500) 
     cv2.destroyWindow('UI AUTO')                  

    except Exception, e:
      print "can't find opencv image"
                   
      print e
def matchrate():
  global start_row,start_col,end_row,end_col,cropped  
  for i in range(1,21):
   if 1<=i<6:
      start_row=int(0)
      start_col=int(sw*(i-1))
      end_row=int(sh)
      end_col=start_col+int(sw)       
      cropped = image[start_row:end_row , start_col:end_col]   
      cv2.imwrite(imagepath+'%s.png'%i,cropped)
      match_img(imagepath+'%s.png'%i)
      
   elif 6<=i<11:
      start_row=sh
      start_col=int(sw*(i-6))
      end_row=int(sh)*2
      end_col=start_col+int(sw)          
      cropped = image[start_row:end_row , start_col:end_col]   
      cv2.imwrite(imagepath+'%s.png'%i,cropped)
      match_img(imagepath+'%s.png'%i)
      
   elif 11<=i<16:
      start_row=sh*2
      start_col=int(sw*(i-11))
      end_row=sh*3
      end_col=start_col+int(sw)          
      cropped = image[start_row:end_row , start_col:end_col]   
      cv2.imwrite(imagepath+'%s.png'%i,cropped)
      match_img(imagepath+'%s.png'%i)
      
   else :
      start_row=sh*3
      start_col=int(sw*(i-16))
      end_row=int(sh)*4
      end_col=start_col+int(sw) 
      cropped = image[start_row:end_row , start_col:end_col]   
      cv2.imwrite(imagepath+'%s.png'%i,cropped)
      match_img(imagepath+'%s.png'%i)

     
matchrate()      
cv2.putText(image, "Result: %s%%"%(totalrate*100), (200,200),cv2.FONT_HERSHEY_COMPLEX, 1, (0,20,220), 2, 8,0) 
cv2.imshow('matchrate',image)
cv2.waitKey(0) 
cv2.destroyWindow('matchrate') 
