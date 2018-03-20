import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  DW96P  DW96W
DW24P  DW24P  DW24P  DW24P  DW96P  DW96W
DW24P  DW24P  DW24P  DW24P  DW96P  DW96W
BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

# Assume there is a Pellet PLUS 500 ul of SIS solution in each well
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [2,3,4,5]:
	for row in [0,1,2]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)

		# pick up 2 * 250ul of SDS from C7, add to C2-5
		position(row,7,position = OffsetDict[offset])
		aspirate(250,depth=97,speed=50, mix=0)
		position(row,col)
		dispense(250, depth=99, speed=100)

		position(row,7,position = OffsetDict[offset])
		aspirate(250,depth=99,speed=50, mix=0)
		position(row,col)
		dispense(250, depth=85, speed=100)
		
		# initial mix
		position(row,col)
		aspirate(330, depth=97,speed=100, mix=0)
		position(row,col)
		dispense(330, depth=100, speed=100)
		position(row,col)
		mix(330,100,100,5)

		# from DW24 to empty DW96
		position(row,col)
		aspirate(300, depth=100,speed=75, mix=0)
		position(row,6,position = OffsetDict[row])
		dispense(300, depth=80, speed=50)
		position(row,col)
		mix(330,100,100,5)
		position(row,col)
		aspirate(300, depth=101,speed=75, mix=0)
		position(row,6,position = OffsetDict[row])
		dispense(300, depth=70, speed=50)
					
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

