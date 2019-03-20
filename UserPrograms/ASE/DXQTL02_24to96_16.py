import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W
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

for col in [2,3,4,5]:
	for row in [0,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 95 + row*2

		# pick up 3 * 320ul of 1xTE from C7, add to C2-5
		position(col-2,7,position = OffsetDict[row])
		aspirate(320,depth= adjusted_depth-25,speed=75, mix=0)
		position(row,col)
		dispense(320, depth=adjusted_depth, speed=100)

		position(col-2,7,position = OffsetDict[row])
		aspirate(320,depth= adjusted_depth-15,speed=75, mix=0)
		position(row,col)
		dispense(320, depth=adjusted_depth, speed=100)

		position(col-2,7,position = OffsetDict[row])
		aspirate(320,depth= adjusted_depth-5,speed=75, mix=0)
		position(row,col)
		dispense(320, depth=adjusted_depth, speed=100)
		
		# initial mix
		position(row,col)
		aspirate(320, depth=adjusted_depth+2,speed=100, mix=0)
		position(row,col)
		dispense(320, depth=adjusted_depth+2, speed=100)
		position(row,col)
		mix(320,adjusted_depth+6,100,5)

		# from DW24 to empty DW96W at c6
		position(row,col)
		aspirate(320, depth=adjusted_depth+6,speed=75, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(320, depth=adjusted_depth+1, speed=50)
		position(row,col)
		mix(320,adjusted_depth+6,100,2)
		position(row,col)
		aspirate(320, depth=adjusted_depth + 6,speed=75, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(320, depth=adjusted_depth+1, speed=50)
		position(row,col)
		mix(320,adjusted_depth+7,100,2)
		aspirate(320, depth=adjusted_depth + 7,speed=75, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(320, depth=adjusted_depth+1, speed=50)
					
		#disposeTips()
		manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

