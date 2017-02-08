with open("copy.txt", 'r') as ip:
	x = ip.read()

print(x.count('['))
print(x.count(']'))
print(x.count(' '))
