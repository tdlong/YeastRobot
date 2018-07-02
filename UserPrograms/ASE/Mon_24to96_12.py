import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

# Assume there is a Pellet PLUS 1 mL of spo solution in each well
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1
adjusted_depth = 95 + row

for col in [2,3,4]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()

		# transfer 3X 330 from DW24P to WASTE#1 at col 6
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=95)
		
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=85)
		
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=75)

		# pick up 2 * 250ul of SIS from C7, add to C2-5
		position(col-2,7,position = OffsetDict[row])
		aspirate(250,depth=97,speed=50, mix=0)
		position(row,col)
		dispense(250, depth=99, speed=100)

		position(col-2,7,position = OffsetDict[row])
		aspirate(250,depth=99,speed=50, mix=0)
		position(row,col)
		dispense(250, depth=85, speed=100)
		
		# initial mix
		position(row,col)
		aspirate(320, depth=97,speed=100, mix=0)
		position(row,col)
		dispense(320, depth=100, speed=100)
		position(row,col)
		mix(320,100,100,5)

		# from DW24 to empty DW96P at c8
		position(row,col)
		aspirate(300, depth=adjusted_depth + 3,speed=75, mix=0)
		position(col-2,8,position = OffsetDict[row])
		dispense(300, depth=80, speed=50)
		position(row,col)
		mix(320,98,100,2)
		position(row,col)
		aspirate(300, depth=adjusted_depth + 4,speed=75, mix=0)
		position(col-2,8,position = OffsetDict[row])
		dispense(300, depth=70, speed=50)
					
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

