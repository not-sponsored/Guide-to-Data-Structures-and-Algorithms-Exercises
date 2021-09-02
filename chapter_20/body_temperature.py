# Answer to exercise 5 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

import sys

def sort_body_temperature(array: list, lower_temperature: int=970,
			  upper_temperature: int=991,
			  step: int=1, divisor=10): 
	"""given array of temps between 97.0 and 99.0 sort in O(N) time
	note that the temperatures are multiplied by a factor of ten in
	order for the range to work
	""" 
	temperature_map = {(i/divisor):0 for i in\
			   		 range(lower_temperature,
					       upper_temperature, step)}

	for temperature in array:
		temperature_map[temperature] += 1

	sorted_temperatures = []
	for temperature, appearances in temperature_map.items():
		sorted_temperatures.extend([temperature] * appearances)

	return sorted_temperatures 	

def main(array: list):
	print(f'Temperatures between 97.0 and 99.0 given as: {array}')
	print(f'sorted in O(N) time as {sort_body_temperature(array)}')

if __name__ == "__main__":
        # example usage:
	# $python body_temperature.py 98.6,98.0,97.1
	# -> Temperatures between 97.0 and 99.0 given as: [98.6, 98.0, 97.1]
	# -> sorted in O(N) time as [97.1, 98.0, 98.6]
	# argv[1] is a list of floats between 97.0 and 99.0 separated by commas
        # with no spaces 
	main([float(x) for x in sys.argv[1].split(',')])
