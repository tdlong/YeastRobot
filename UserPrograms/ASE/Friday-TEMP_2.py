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

myvol = 140
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

for col in [3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)

                # transfer 3X 330 from DW24P to WASTE#1 at col 6
		position(row,col)
		aspirate(330, depth=95)
		position(col-2,6, position = OffsetDict[row])
		dispense(330, depth=65)
		
		position(row,col)
		aspirate(330, depth=96)
		position(col-2,6, position = OffsetDict[row])
		dispense(330, depth=60)
		
		position(row,col)
		aspirate(330, depth=96)
		position(col-2,6, position = OffsetDict[row])
		dispense(330, depth=45)
		
		# add spo or ynbd at c8 to DW24			
		position(col-2,8, position = OffsetDict[row])
		aspirate(330,depth=80)
		position(row, col)
		dispense(330,depth=90)
		position(col-2,8, position = OffsetDict[row])
		aspirate(330,depth=85)
		position(row, col)
		dispense(330,depth=90)
		position(col-2,8, position = OffsetDict[row])
		aspirate(330,depth=98)
		position(row, col)
		dispense(330,depth=90)

		mix(330,98,100,5)
		
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

