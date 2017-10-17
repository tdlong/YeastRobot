import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
RES41	SW24P  SW24P  SW24P  SW24P  RES41
RES41	SW24P  SW24P  SW24P  SW24P
RES41	SW24P  SW24P  SW24P  SW24P
RES41	SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.

position(0,0)

targetSpeed = int(ezFast * 0.01)
volume = int(500 * stepsPerUL)

while True:
	print("please enter a single letter corresponding to where you want the \"D\" axis")
	print("h = home;  e = eject;  z = plunger neutral;  f = 500 ul;  q = quit")
	inp = raw_input()
	print(inp)
	if inp == "" or inp == "q":
		break
	elif inp == "h":
		EZ_GoTo_A(0, 200)
	elif inp == "e":
		EZ_GoTo_A(6000, 200)
	elif inp == "z":
		EZ_GoTo_A(plungerLimit, 200)
	elif inp == "f":
		EZ_GoTo_A(plungerLimit - volume, 200)
																					
InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
