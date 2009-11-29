#!/usr/bin/python
# -*- coding: utf-8 -*-

#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

from PIL import Image
from sys import argv

class invader():

    def __init__(self, seed, bgcolor=(0,0,0,0), color=(0,0,0,255), x=3, y=5):
        self.pixels = Image.new("RGBA", [x*2,y], bgcolor)

        seed_upper_bound = 2**(x*y)-1
        if seed > seed_upper_bound:
            raise Exception, "Seed can only be as large as " + str(seed_upper_bound) + "."
        else:
            self.seed = seed

        # fill with seed (little baby invaders are made this way)
        for xcoord in range(x):
            for ycoord in range(y):
                # check if binary value is uneven
                if seed % 2 == 1:
                    # put pixel
                    self.pixels.putpixel([x-1-xcoord,ycoord], color)
                    # put mirror pixel
                    self.pixels.putpixel([x+xcoord,ycoord], color)
                seed = seed >> 1

    def save(self):
        filename = str(self.seed)
        self.pixels.save(filename + ".png", "PNG")

if __name__ == '__main__':
    if len(argv) < 2 or len(argv) > 3 :
        print """Usage:
            every-possible-space-invader [seed]
            every-possible-space-invader [start-seed] [end-seed]"""
    elif len(argv) <3: # this is love
        a = invader(int(argv[1]))
        a.save()
    elif len(argv) == 3:
        start = int(argv[1])
        end = int(argv[2])
        for i in range(start, end+1):
            a = invader(i)
            a.save()
