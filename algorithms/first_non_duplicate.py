import sys

def first_non_dupe(arr):
	"""find missing letter in string"""
	in_str = str(arr).lower()
	map = {}
	for char in in_str:
		map[char] = map.get(char, 0) + 1 
	for char,num in map.items():
		if num <= 1:
			print(char)
			break 
	return

if __name__ == "__main__":
	first_non_dupe(sys.argv[1])
