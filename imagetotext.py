import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import sys

im = Image.open(sys.argv[1])

arg = None
if len(sys.argv) > 2:
	arg = sys.argv[2]

im_grey = im.convert('L') #convert the image to greyscale
if arg is None:
	im_array = np.array(im)
else:
	im_array = np.array(im_grey)
print(im_array)
print(im_array.shape)
np.savetxt('data/frac/input.txt', im_array, fmt='%s')
pl.imshow(im_array, cmap=arg)
pl.show() 
