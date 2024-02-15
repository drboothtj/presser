'''
Presser.py will push random keys from the KEY set.
NOTE: This doesn't work well from WSL. If using windows I reccommend runnin in PowerShell.
	Arguments: None
'''
##TODO##
#Implement pressing multiple keys
#Implement some other input modes then random
#Implement parser with some options (read from file, keys, sleep time, mode)
#Implement some limits to the run loop, time or number of presses
#Organise into scripts
#quiet and noisy output


KEYS = ['a', 'b']
SLEEP_TIME = 3

import random
from pyautogui import press
from time import sleep


def get_random_key():
	'''
	get a random key from the KEYS list to press
		arguments:
			None
		returns:
			key: string reprisenting a key to be pressed
	'''
	key = random.choice(KEYS)
	print(f'chose to press {key}')
	return key

def press_key(key):
	'''
	use pynput package to press the provided key
		arguments:
			key: the key to simulate pressing
		returns:
			None
	'''
	print(f'Pressing {key}')
	press(key)

def main():
	'''
	main routine for presser.py
	'''
	print(f'Presser has initialised. You have {SLEEP_TIME} seconds before it begins.')
	#waiting time is used for safety
	sleep(SLEEP_TIME)
	print('Pressing keys now!') #maybe we can add a sound somehow
	for i in range(10): #change to infinite, maybe implemtn character or time variables
		key = get_random_key() #this could be replaced with anything really simple AI, text parser etc.
		press_key(key) #make it handle multiple keys at a time
main()
