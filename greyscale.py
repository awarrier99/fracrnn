import pylab as pl
import matplotlib.cm as cm
import numpy as np
from PIL import Image

im = Image.open('fractal1.jpg')
im_grey = im.convert('L') #convert the image to greyscale
im_array = np.array(im_grey)
print(im_array)
np.savetxt('fractaldata.txt', im_array,fmt='%s')
pl.imshow(im_array, cmap=cm.Greys_r)
pl.show() 
