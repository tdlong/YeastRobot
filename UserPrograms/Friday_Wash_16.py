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
		
		# transfer 3X 300 from DW24P to WASTE#1 at col 6
		position(row,col)
		aspirate(300, depth=95)
		position(col-2,6, position = OffsetDict[row])
		dispense(300, depth=95)
		
		position(row,col)
		aspirate(300, depth=95)
		position(col-2,6, position = OffsetDict[row])
		dispense(300, depth=90)
		
		position(row,col)
		aspirate(300, depth=95)
		position(col-2,6, position = OffsetDict[row])
		dispense(300, depth=85)
		
		# add water from DW96W at 8 to DW24, then suck off water and discard at Column 7
		# at speed 25 depth 90 still eats up pellet may need to add h2o manually in robot hood
		# then spin down and use robot to discard the supernatant and resuspend in spo
		# can also try leaving the last couple hundred uL of YPD in wells to absorb droplets during wash
		# Not working, no matter how slow or what height, so maybe just resuspend and spin down
		for i in [55,65,75,85,95,99]:
			position(col-2,8, position = OffsetDict[row])
			aspirate(320,depth=i)
			position(row, col)
			dispense(320,depth=95)
			
		mix(330,98,100,3)
			
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

