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
CurrentTipPosition = 2

for col in [2]:
	for row in [0]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth_row = 95 + row*2
		adjusted_depth_column = 95 + (col - 2)*2

		# pick up 1 * 320ul of 1xTE from C7, add to C2-5
		position(col-2,7,position = OffsetDict[row])
		aspirate(320,depth= adjusted_depth_column-8,speed=75, mix=0)
		position(row,col)
		dispense(320, depth=adjusted_depth_row, speed=100)
		
		# initial mix
		position(row,col)
		mix(320,adjusted_depth_row+5-(col-2),100,3)

		# from DW24 to empty DW96W at c6
		position(row,col)
		aspirate(320, depth=adjusted_depth_row+5-(col-2),speed=75, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(320, depth=adjusted_depth_column-2-(col - 2), speed=50)
					
		#disposeTips()
		manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

