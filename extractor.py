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
    _setup_image = None
    _region_size = 16
    _image_display = 'image'

    def __init__(self):
        pass

    def __update_image(self, img):
        cv2.imshow(self._image_display, img)

    def __draw_region(self, img, coords, size):
        region_image = np.array(img)
        pt2 = (coords[0] + size, coords[1] + size)
        cv2.rectangle(region_image, coords, pt2, (0, 255, 255))
        self.__update_image(region_image)

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

        if (self._last_coords):
            self.__draw_region(self._setup_image, self._last_coords, self._region_size)

    def __choose_region(self, img):
        self._setup_image = img
        cv2.imshow(self._image_display, img)
        cv2.setMouseCallback(self._image_display, self.__handle_mouse)

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




