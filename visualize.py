# -*- coding: utf-8 -*-

import csv
import numpy
import matplotlib.pyplot as plt

def visualize(csvfilename):
	print csvfilename
	letters = []
	states = []

	with open(csvfilename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		count = 0        
		for row in spamreader:
			count+=1
			if count > 1900:
				if len(row)>1:              
					letters.append(row[0])
					values = []
					for j in range(1,len(row)):
						values.append(float(row[j]))
					states.append(values)	    

	table = numpy.asarray(states)    
	table = table - numpy.mean(table,axis=0)
	table = table/numpy.std(table,axis=0)        
	plt.figure(figsize=[22,8])
	plt.imshow(table.T,interpolation='None')
	plt.colorbar()
	plt.xticks(numpy.arange(len(letters)),letters,fontsize=8)
	plt.savefig(csvfilename + '.png')
	plt.close()
	print 'Done ' + csvfilename + '.'

visualize('cstates.csv')
visualize('hstates.csv')
