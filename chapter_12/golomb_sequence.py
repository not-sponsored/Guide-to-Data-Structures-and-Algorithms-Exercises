# Answer to exercise 2 in chapter 12 
#
# Exercise/code from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def golomb(n: int, map={}):
	"""memoized recursive generation of Nth number in Golomb sequence"""
	if n == 1:
		return 1
	if n not in map:
		map[n] = 1 + golomb(n - golomb(golomb(n - 1)))
	return map[n]

def main(n: str):
	print(f'{n} number in the Golomb sequence: {golomb(int(n))}')

if __name__ == '__main__':
	# Example usage:
        # $python golomb_sequence.py 9 
        # -> 9 number in the Golomb sequence: 5 
        # argv[1] is a int of the Nth position in the sequence 
	main(sys.argv[1])
