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

myvol = 140
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

for col in [2]:
	counter = 2
	for tip in [9,13]:
		counter += 1
		CurrentTipPosition = tip

		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 97 + (counter-1)*2

		# transfer 3X 330 from DW24P to WASTE#1 at col 6
		position(counter-1,col)
		aspirate(320, depth=adjusted_depth)
		position(counter-1,6, position = OffsetDict[0])
		dispense(320, depth=95)
		
		position(counter-1,col)
		aspirate(320, depth=adjusted_depth)
		position(counter-1,6, position = OffsetDict[0])
		dispense(320, depth=85)
		
		position(counter-1,col)
		aspirate(320, depth=adjusted_depth)
		position(counter-1,6, position = OffsetDict[0])
		dispense(320, depth=75)

		# add 3x330uL smqH2O at c7 to DW24			
		position(counter-1,7, position = OffsetDict[0])
		aspirate(320,depth=75)
		position(counter-1, col)
		dispense(320,depth=adjusted_depth)
		position(counter-1,7, position = OffsetDict[0])
		aspirate(320,depth=85)
		position(counter-1, col)
		dispense(320,depth=adjusted_depth)
		position(counter-1,7, position = OffsetDict[0])
		aspirate(320,depth=95)
		position(counter-1, col)
		dispense(320,depth=adjusted_depth)
		
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

