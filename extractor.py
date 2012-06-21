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
TARGET_FILES_ARG = 'target file prefix'

class Extractor(object):
    _mouse_down = False
    _last_coords = (0, 0)
    _setup_image = None
    _region_size = 32
    _image_display = 'image'
    _files = None
    _current_index = 0

    def __init__(self, files):
        self._files = files
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

    def __show_image(self):
        img = cv2.imread(self._files[self._current_index])
        self._setup_image = img
        cv2.imshow(self._image_display, img)

    def __select_region(self):

        while(True):
            ch = cv2.waitKey()
            if ch == 27:
                break
            if chr(ch) in ('j', 'k', '0'):
                i = self._current_index

                if ch == ord ('0'):
                    i = 0
                elif ch == ord('j'):
                    i = i - 1 if i > 0 else len(self._files) - 1
                elif ch == ord('k'):
                    i = i + 1 if i < len(self._files) - 1 else 0

                self._current_index = i
                self.__show_image()
                self.__draw_region(self._setup_image, self._last_coords,
                                   self._region_size)

        return self._last_coords

    def start_selection(self):
        # Use first image to get user's input
        cv2.namedWindow(self._image_display)
        cv2.setMouseCallback(self._image_display, self.__handle_mouse)
        self.__show_image()
        coords = self.__select_region()
        return coords


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                        description='Extract similar regions from' + 
                                     'a sequence of images')
    parser.add_argument(IMAGE_FILES_ARG, nargs='+')
    parser.add_argument(TARGET_FILES_ARG, nargs=1)
    args = vars(parser.parse_args())
    files = args[IMAGE_FILES_ARG]
    prefix = args[TARGET_FILES_ARG]

    ext = Extractor(files)
    coords = ext.start_selection()

    # ext.extract_images(coords, 




