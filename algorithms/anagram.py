import sys

def anagram(ana):
	# base only single char
	if len(ana) == 1:
		return [ana[0]]

	# create an array to hold the anagrams
	collection = []

	# find all anagrams of the substring from the second char until end
	# for "abcd" substr "bcd" 
	sub_anag = anagram(ana[1:])
	
	# iterate over each substr
	for sub in sub_anag:
		
		# insert first char into each index
		for index in range(0, len(sub)+1):
			collection.append(sub[:index] + ana[0] + sub[index:])
	return collection 

def main(ana):
	print(anagram(ana))

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(str(sys.argv[1]))
