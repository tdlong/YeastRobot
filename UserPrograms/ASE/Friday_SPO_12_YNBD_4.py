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

for col in [2,3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 95 + row*2

        # transfer 3X 330 from DW24P to WASTE#1 at col 6
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=75)
		
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=70)
		
		position(row,col)
		aspirate(320, depth=adjusted_depth)
		position(col-2,6, position = OffsetDict[row])
		dispense(320, depth=65)
		
		# add spo or ynbd at c8 to DW24			
		position(col-2,8, position = OffsetDict[row])
		aspirate(320,depth=75+row, speed = 100)
		position(row, col)
		dispense(320,depth=adjusted_depth, speed = 100)
		position(col-2,8, position = OffsetDict[row])
		aspirate(320,depth=85+row, speed = 100)
		position(row, col)
		dispense(320,depth=adjusted_depth, speed = 100)
		position(col-2,8, position = OffsetDict[row])
		aspirate(320,depth=95+row, speed = 100)
		position(row, col)
		dispense(320,depth=adjusted_depth, speed = 100)

		mix(320,adjusted_depth,100,5)
		
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

