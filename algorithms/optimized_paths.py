import sys

def num_uni(row, col, map={}):
	if row == 1 or col == 1:
		return 1
	if not (row, col) in map:
		map[(row, col)] = num_uni(row - 1, col, map) +\
		num_uni(row, col - 1, map)
	return map[(row, col)]

def main(row, col):
	print(num_uni(row, col))

if __name__ == '__main__':
	main(int(sys.argv[1]), int(sys.argv[2]))
