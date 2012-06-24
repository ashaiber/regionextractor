import cv2
import numpy as np
import pdb
import math
import os

class Collager(object):
    _files = None 
    _region_size = 0
    _border_width = 1

    def __init__(self, files, region_size):
        self._files = files
        self._region_size = region_size
        pass

    def __extract_region(self, im, coords, region_size):
        return im[coords[1] : coords[1] + region_size,
                  coords[0] : coords[0] + region_size, :]

    def show_collage(self, coords):
        # Open first image to determine type and #channels
        im = cv2.imread(self._files[0])
        dtype = im.dtype


        imcount = len(self._files)
        region_per_side = (math.ceil(imcount**0.5))
        collage_size = (region_per_side - 1) *  \
                       (self._region_size + self._border_width) + \
                       self._region_size

        collage = np.zeros((collage_size, collage_size, im.shape[2]), dtype = dtype)
        collage[:,:] = (0, 255, 255)

        count = 0
        for f in self._files:
            im = cv2.imread(f)
            x = count % region_per_side
            y = int(count / region_per_side)
            region = self.__extract_region(im, coords, self._region_size)
            collage[y * (self._region_size + 1):(y + 1) * (self._region_size + \
                                                           1) - 1,
                    x * (self._region_size + 1):(x + 1) * (self._region_size + \
                                                           1) - 1] =  region
            count += 1

        return collage

    def save_collage(self, coords, prefix):
        count = 0
        # Determine prefix for files (to avoid overwriting existing)
        if (os.path.exists("%s_000.png" % prefix)):
            suf = ord('a')
            newprefix = prefix + chr(suf)
            while os.path.exists("%s_000.png" % newprefix):
                suf += 1
                newprefix = prefix + chr(suf)

            prefix = newprefix

        # Save image files and aggregate measurements table
        for f in self._files:
            im = cv2.imread(f)
            region = self.__extract_region(im, coords, self._region_size)
            cv2.imwrite(prefix + '_' + "%03d" % count + '.png', region)
            count += 1

        print("Saved %d images to %s*" % (count, prefix))
        return prefix


