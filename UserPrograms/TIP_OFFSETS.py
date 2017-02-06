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

CurrentTipPosition = 1																	
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.
position(1,2)
enterToContinue()

for row in [1]:
#	for col in [3,4,5,6]:
	for col in [3,4]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
		enterToContinue()
		position(1,2)																		
		aspirate(myvol, 75, 7)				# Aspirate(volume,% to bottom,speed)
		enterToContinue()
		position(row,col)																		
		dispense(myvol, 95, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()

																					
InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
