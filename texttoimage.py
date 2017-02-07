import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import sys

fname = sys.argv[1]
print("Importing image data from file " + fname + "...")
im_array = np.genfromtxt(fname)

pl.imshow(im_array, cmap=cm.Greys_r)
pl.savefig("images/" + fname[:-4] + sys.argv[2] + '.png')
print("Saved figure")
pl.show() 
