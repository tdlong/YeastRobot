import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW96W  DW96W  DW96W  BLANK
DW24P  BLANK  BLANK  BLANK  BLANK
DW24P  BLANK  BLANK  BLANK  BLANK
DW24P  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [2]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)

		# transfer 3X 330 from DW24P to WASTE at c4
		position(row,col)
		aspirate(330, depth=95)
		position(col-2,4, position = OffsetDict[row])
		dispense(330, depth=95)
		
		position(row,col)
		aspirate(330, depth=95)
		position(col-2,4, position = OffsetDict[row])
		dispense(330, depth=85)
		
		position(row,col)
		aspirate(330, depth=95)
		position(col-2,4, position = OffsetDict[row])
		dispense(330, depth=75)

        # transfer 300uL YPDa from DW96W reservoir at c5 to DW24P at c2
		position(col-2,5,position = OffsetDict[row])
		aspirate(300,depth=99,speed=50, mix=0)
		position(row,col)
		dispense(300, depth=98, speed=50)

		# mix
		position(row,col)
		mix(250,99,100,5)

		# 250 from DW24P at c2 to DW96W at c3
		position(row,col)
		aspirate(250,depth=99,speed=50, mix=0)
		position(col-2,3,position = OffsetDict[row])
		dispense(250, depth=97, speed=50)
				
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

