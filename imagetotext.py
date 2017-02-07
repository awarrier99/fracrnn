import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import sys

im = Image.open(sys.argv[1])
im_grey = im.convert('L') #convert the image to greyscale
im_array = np.array(im_grey)
print(im_array)
np.savetxt('data/frac/input.txt', im_array,fmt='%s')
pl.imshow(im_array, cmap=cm.Greys_r)
pl.show() 
