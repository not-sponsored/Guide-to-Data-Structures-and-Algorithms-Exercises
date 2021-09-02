import sys
import os

def find_directories(directory):
	for dirpath, dirs, files in os.walk(str(directory)):
		for dr in dirs:
			print(dr)

if __name__ == '__main__':
	find_directories(sys.argv[1])
	

