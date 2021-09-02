import sys

def sum_arr(arr):
	if len(arr) == 1:
		return arr[0]
	else:
		return arr[0] + sum_arr(arr[1:])

def main(arr):
	print(sum_arr([int(x) for x in arr]))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(str(sys.argv[1]).split(','))
