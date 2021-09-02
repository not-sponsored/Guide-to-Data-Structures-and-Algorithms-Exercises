import sys

def cnt_x(arr):
	if len(arr) == 1:
		return int(arr[0] == 'x')
	else:
		return cnt_x(arr[1:]) + int(arr[0] == 'x') 

def main(arr):
	print(cnt_x(arr.lower()))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(str(sys.argv[1]))
