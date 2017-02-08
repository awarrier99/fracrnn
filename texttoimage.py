import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image
import sys

fname = sys.argv[1]
print("Importing image data from file " + fname + "...")
im_array = np.genfromtxt(fname)

arg = None
if len(sys.argv) > 3:
	arg = sys.argv[3]

im = fromarray(np.uint8(im_array))
im.save("images/" + fname[:-4] + sys.argv[2] + '.png')
print("Saved figure")
