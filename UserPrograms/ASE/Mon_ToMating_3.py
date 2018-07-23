import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  DW96W  DW96W BLANK BLANK BLANK BLANK
DW96W  DW96W  DW96W BLANK BLANK BLANK BLANK
DW96W  DW96W  DW96W BLANK BLANK BLANK BLANK 
BLANK  BLANK  BLANK BLANK BLANK BLANK BLANK
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


# eventually row in 0,1,2,3
for row in [0,1,2]:
	for offset in [0,1,2,3]:
		# get tips
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 95 + row

		#aspirate 330 ul of YPD (C2) -> discard to DW96W at C3
		position(row,2,position = OffsetDict[offset])
		aspirate(320,depth=adjusted_depth,speed=50, mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(320, depth=80, speed=50)
		
			
		# pick up 250ul of YPD from C4, add to C2
		position(row,4,position = OffsetDict[offset])
		aspirate(250,depth=adjusted_depth,speed=50, mix=0)
		position(row,2,position = OffsetDict[offset])
		dispense(250, depth=adjusted_depth, speed=50)
		
		# discard tips
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

