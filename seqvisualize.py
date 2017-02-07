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
		for row in spamreader:
			if len(row)>1:              
				letters.append(row[0])
				values = []
				for j in range(1,len(row)):
					values.append(float(row[j]))
				states.append(values)	    


	states = [i - numpy.mean(states) for i in states]
	states = [i / numpy.std(states) for i in states]
	table = numpy.asarray(states)    
	plt.figure(figsize=[6,12])
	plt.imshow(table.T,interpolation='None')
	plt.colorbar()
	plt.xticks(numpy.arange(len(letters)),letters,fontsize=8)
	plt.savefig(csvfilename + '.png')
	plt.close()
	print 'Done ' + csvfilename + '.'

visualize('seq1cstates.csv')
visualize('seq2cstates.csv')
visualize('seq3cstates.csv')
visualize('seq1hstates.csv')
visualize('seq2hstates.csv')
visualize('seq3hstates.csv')
