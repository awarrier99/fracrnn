with open("data/frac/input.txt", 'r') as ip:
	x = ip.read()
	x = x.replace('[', '')
	x = x.replace(']', '')
	

with open("data/frac/input.txt", 'w') as op:
	op.write(x)

