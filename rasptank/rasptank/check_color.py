import sys
import time
import rclpy
from rclpy.node import Node
from enum import IntEnum, auto

from geometry_msgs.msg import Twist
from rasptank_msgs.srv import Grub, Release

import numpy as np

import cv2

from .control_modules.RPIservo import *

WIDTH = 640
HEIGHT = 480

ksize = 9

speed_set = 40

class ColorTracking(Node):
    def __init__(self):
        super().__init__(node_name = 'grub_object')
        

    
        
    def calc_outline(self, img):
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
        #print(img_hsv)
        hsv = [230,140,160]
        h = img_hsv[:, :, 0]
        s = img_hsv[:, :, 1]
        v = img_hsv[:, :, 2]
        
        #img_copy = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        #print(img_copy)
        
        '''
        h_max = hsv[0]+10
        h_min = hsv[0]-10
        
        if h_max>255:
            h_max = 255
        elif h_min<0:
            h_min = 0
            
        s_max = hsv[1]+60
        s_min = hsv[1]-60
        
        if s_max>255:
            s_max = 255
        elif s_min<0:
            s_min = 0
            
        v_max = hsv[2]+100
        v_min = hsv[2]-100
        
        if v_max>255:
            v_max = 255
        elif v_min<0:
            v_min = 0
        '''    
        
        #hsv_max = (int(h_max), int(s_max), int(v_max))
        #hsv_min = (int(h_min), int(s_min), int(v_min))
        
        hsv_max = (int(hsv[0]+1), int(hsv[1])+10, int(hsv[2])+100)
        hsv_min = (int(hsv[0]-1), int(hsv[1])-10, int(hsv[2])-100)
        
        img_gray = cv2.inRange(img_hsv, hsv_min, hsv_max)    # HSV‚©‚çƒ}ƒXƒN‚ðì¬
        img_mask = cv2.medianBlur(img_gray,ksize)
        cv2.imwrite('gray_pic.jpg', np.array(img_gray))
        cv2.imwrite('mask_pic.jpg', np.array(img_mask))
        
        M = cv2.moments(img_mask, False)
        #contours, hierarchy = cv2.findContours(img_gray, cv2. RETR_EXTERNAL, cv2.CHIN_APPROX_SIMPLE)
        
        if M["m00"]==0:
          x = -1
          y = -1
          return x,y
        else:
          x,y = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
          return x, y
          

def main(args=None):
    rclpy.init(args=args)
    
    colortracking = ColorTracking()

    img = cv2.imread("/home/ubuntu/ros2/get_pic.jpg")
    colortracking.calc_outline(img)

    
    
    rclpy.shutdown()

