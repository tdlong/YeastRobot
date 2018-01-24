import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W  DW96W
DW24P  DW24P  DW24P  DW24P  DW96W  DW96W  DW96W  DW96W
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

# Assume there is a Pellet PLUS 1 ml of solution in each well of DW24P
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [2,3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# transfer 6X 330 from DW24P to WASTE#2 at col 7
		for i in [95,85,75,65,55,35]:
			position(row,col)
			aspirate(330, depth=95)
			position(col-2,6, position = OffsetDict[row])
			dispense(330, depth=i)
			
		# add spor media at 9 to DW24 and mix			
		position(col-2,9, position = OffsetDict[row])
		aspirate(330,depth=75)
		position(row, col)
		dispense(330,depth=90)
		position(col-2,9, position = OffsetDict[row])
		aspirate(330,depth=85)
		position(row, col)
		dispense(330,depth=90)
		position(col-2,9, position = OffsetDict[row])
		aspirate(330,depth=98)
		position(row, col)
		dispense(330,depth=90)
		
		mix(330,98,100,10)
							
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

