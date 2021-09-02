import sys

def rec_str(arr):
	if len(arr) == 1:
		return arr[0]
	else:
		return rec_str(arr[1:]) + arr[0] 

def main(arr):
	print(rec_str(arr))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(str(sys.argv[1]))
