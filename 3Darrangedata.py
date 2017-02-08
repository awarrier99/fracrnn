
print("Shaping data array...")

with open('sample.txt', 'r') as ip:
	raw = ip.read()
	contents = raw.replace('\n', ' ')
	contents = contents.strip()
	aslist = contents.split(' ')

def is_number(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

aslist = [k for k in aslist if is_number(k)]

with open('fractaloutput.txt', 'w') as op:
	for i in range(0, len(aslist)):
		if (i % 3) == 0:
			op.write('[')
		op.write(aslist[i])
		if ((i + 1) % 3) == 0:
			op.write('] ')
		else:
			op.write(' ')
		if ((i + 1) % 768) == 0 and i != 0:
			op.write('\n')

print("Data arranged")
