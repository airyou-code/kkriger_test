import os
import time
import psutil
import cv2
import pyscreenshot as ImageGrab
import keyboard
import sys

class TestGame():
    def __init__(self):
        self.file_path = None
        self.data_path = None
    
    def initTest(self,data_path, file_path):
        self.path_file =  file_path
        self.data_path = data_path

if __name__ == '__main__':
    args = sys.argv[1:]
    path_file = args[0]
    data_path = None
    if args[1] == "-o":
        data_path = args[2]

    test = TestGame()
    test.initTest(data_path, path_file)