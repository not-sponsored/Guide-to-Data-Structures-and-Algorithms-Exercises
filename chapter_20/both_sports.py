# Answer to exercise 1 in chapter 20 
#
# Exercise from: A Common-Sense Guide to Data Structures and Algorithms 
# Level Up Your Core Programming Skills 
# by Jay Wengrow and edited by Brian MacDonald

def get_play_both(basketball: list, football: list): 
	"""given two lists return players that appear in both in O(N+M)""" 
	basketball_map = {f"{player['first_name']} {player['last_name']}":True\
			  for player in basketball}
	overlapping = [] 
	for player in football:
		key = f"{player['first_name']} {player['last_name']}"
		if key in basketball_map:
			overlapping.append(key)
	return overlapping

def main():
	basketball_players = [
		{'first_name': "Jill", 'last_name': "Huang", 'team': "Gators"},
		{'first_name': "Janko", 'last_name': "Barton",
		 'team': "Sharks"},
		{'first_name': "Wanda", 'last_name': "Vakulskas",
		 'team': "Sharks"},
		{'first_name': "Jill", 'last_name': "Moloney",
		 'team': "Gators"},
		{'first_name': "Luuk", 'last_name': "Watkins", 'team': "Gators"}
	]
	football_players = [
		{'first_name': "Hanzla", 'last_name': "Radosti",
		 'team': "32ers"},
		{'first_name': "Tina", 'last_name': "Watkins",
		 'team': "Barleycorns"},
		{'first_name': "Alex", 'last_name': "Patel", 'team': "32ers"},
		{'first_name': "Jill", 'last_name': "Huang",
		 'team': "Barleycorns"},
		{'first_name': "Wanda", 'last_name': "Vakulskas",
		 'team': "Barleycorns"}
	]

	print(f'basketball players: {basketball_players}')
	print(f'football players: {football_players}')
	print('\nThe following players play both: ', end='')
	print(get_play_both(basketball_players, football_players))

if __name__ == "__main__":
        # example usage:
	# $python both_sports.py
	# -> Omitted ...
	# -> The following players play both: ['Jill Huang', 'Wanda Vakulskas']
	main()
