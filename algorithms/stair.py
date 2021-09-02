import sys

def paths(steps):
	# case 1 only one step
	if steps == 1 or steps == 0: 
		return 1 
	elif steps < 0:
		return 0
	else:
		return paths(steps - 1) + paths(steps - 2) + paths(steps - 3) 

def main(arr):
	print(paths(int(arr)))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(str(sys.argv[1]))
