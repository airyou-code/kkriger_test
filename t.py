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
        self.pid = None
    
    def initTest(self,data_path, file_path):
        self.path_file =  file_path
        self.data_path = data_path

    def startGame(self):
        os.startfile(self.path_file)
        check = False
        while True:
            img = ImageGrab.grab()
            img.save(self.data_path + '/main_scene_after_loading.png')
            image = cv2.imread(self.data_path + '/main_scene_after_loading.png')
            (r, g, b) = image[370, 170]
            (r1, g1, b1) = image[170, 370]
            (r2, g2, b2) = image[470, 770]
            (r3, g3, b3) = image[750, 750]
            if (r, g, b) == (255, 255, 255) and \
                    (r1, g1, b1) == (0, 0, 0) and \
                    (r2, g2, b2) == (0, 0, 0) and \
                    (r3, g3, b3) == (0, 0, 0):
                if not check:
                    check = True
                continue
            if check:
                break
        # time.sleep(10)

if __name__ == '__main__':
    args = sys.argv[1:]
    path_file = args[0]
    data_path = None
    if args[1] == "-o":
        data_path = args[2]

    test = TestGame()
    test.initTest(data_path, path_file)
    test.startGame()