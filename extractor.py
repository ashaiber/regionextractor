#!/usr/bin/env python
"""
This program takes a sequence of images, allows the user to select a block from
the first image, and then extracts similar blocks from subsequent images in the
sequence into a new sequence.
"""

import cv2
import numpy as np
import argparse

IMAGE_FILES_ARG = 'image files'

class Extractor(object):
    _mouse_down = False
    _last_coords = None

    def __init__(self):
        pass

    def __handle_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._mouse_down = True
            self._last_coords = (x, y)
            print("click at ({0}, {1})".format(x, y))
        elif event == cv2.EVENT_LBUTTONUP:
            self._mouse_down = False
        elif event == cv2.EVENT_MOUSEMOVE and self._mouse_down:
            self._last_coords = (x, y)
            print("click at ({0}, {1})".format(x, y))

    def __choose_region(self, img):
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', self.__handle_mouse)

        while(True):
            ch = cv2.waitKey()
            if ch == 27:
                break
        return self._last_coords

    def process_images(self, files):
        # Use first image to get user's input
        img = cv2.imread(files[0])
        coords = self.__choose_region(img)


if __name__ == '__main__':
    ext = Extractor()

    parser = argparse.ArgumentParser(
                        description='Extract similar regions from' + 
                                     'a sequence of images')
    parser.add_argument(IMAGE_FILES_ARG, nargs='+')
    args = vars(parser.parse_args())
    files = args[IMAGE_FILES_ARG]

    ext.process_images(files)




