import csv
import numpy
import matplotlib.pyplot as plt

def correlate(csvfilename):
	print csvfilename
	letters = []
	states = []
    
	with open(csvfilename, 'rb') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		count = 0
		for row in spamreader:
			if len(row) > 1:
				letters.append(row[0])
				values = []
				for j in range(1, len(row)):
					values.append(float(row[j]))
				states.append(values)

	seq1 = []
	for i in range(0, len(letters)):
		let = letters[i]
		if let.isupper() and ((i == 0) or (letters[i - 1].islower())):
			seq1.append(1)
		else:
			seq1.append(0)

	seq2 = []
	seq2.append(0)
	for i in range(1, len(letters)):
		let = letters[i]
		plet = letters[i - 1]
		if let.islower() and plet.isupper():
			seq2.append(1)
		else:
			seq2.append(0)


	seq3 = []
	for i in range(0, len(letters)):
		let = letters[i]
		if let.isupper():
			seq3.append(1)
		else:
			seq3.append(0)
	
	unpacked = []
	for i in range(0, len(states[0])):
		tmp = []
		for j in range(0, len(states)):
			tmp.append(states[j][i])
		unpacked.append(tmp)

	corrs1 = []
	corrs2 = []
	corrs3 = []
	for i in range(0, len(unpacked)):
		curstates = unpacked[i]
		corrs1.append(numpy.corrcoef(curstates, seq1))
		corrs2.append(numpy.corrcoef(curstates, seq2))
		corrs3.append(numpy.corrcoef(curstates, seq3))
	
	output = "Seq1"
	for i in range(0, len(corrs1)):
		output += "," + str(corrs1[i][0][1])
	with open("seq1" + csvfilename, 'w') as op:
		op.write(output)

	print 'Done seq1' + csvfilename + '.'

	output = "Seq2"
	for i in range(0, len(corrs2)):
		output += "," + str(corrs2[i][0][1])
	with open("seq2" + csvfilename, 'w') as op:
		op.write(output)

	print 'Done seq2' + csvfilename + '.'

	output = "Seq3"
	for i in range(0, len(corrs3)):
		output += "," + str(corrs3[i][0][1])
	with open("seq3" + csvfilename, 'w') as op:
		op.write(output)

	print 'Done seq3' + csvfilename + '.'

correlate('hstates.csv')
correlate('cstates.csv')
