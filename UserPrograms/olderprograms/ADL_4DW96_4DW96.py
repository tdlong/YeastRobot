import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  DW24P
DW96P  DW24P
DW96P  DW24P
DW96P  DW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.
position(1,2)
enterToContinue()

#4_DW96 to 4_DW96 (500 ul)
for row in [0,1,2,3]:
	for off in [1,2,3,4]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(row,2,off)																		
		moveAspirate(myvol, 20, 70, 20)				# Aspirate(volume,% to bottom,speed)
		position(row,3,off)		
		# def moveDispense(vol, startdepth = 100, speed = 100, blowout = 'N'):
		moveDispense(myvol, 80, 20, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()
InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
