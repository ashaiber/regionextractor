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

def choose_region(img):
    cv2.imshow('image', img)

    while(True):
        ch = cv2.waitKey()
        if ch == 27:
            break


def process_images():
    parser = argparse.ArgumentParser(
                        description='Extract similar regions from' + 
                                     'a sequence of images')
    parser.add_argument(IMAGE_FILES_ARG, nargs='+')
    args = vars(parser.parse_args())

    files = args[IMAGE_FILES_ARG]

    # Use first image to get user's input
    img = cv2.imread(files[0])
    coords, size = choose_region(img)



if __name__ == '__main__':
    process_images()
