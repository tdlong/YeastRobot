import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
#16_SW24 to 16_SW24 (20 ul)
deck="""\
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.
position(1,2)
enterToContinue()


for row in [0,1,2,3]:
	for col in [2,3,4,5]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(row,col)																		
		aspirate(20, 90, 7)				# Aspirate(volume,% to bottom,speed)
		position(row,col+4)																		
		dispense(20, 90, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()


InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
