import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  DW96W  DW96W BLANK BLANK BLANK BLANK 
DW96P  DW96W  DW96W BLANK BLANK BLANK BLANK 
DW96P  DW96W  DW96W BLANK BLANK BLANK BLANK  
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

		#aspirate 2 x 250 ul of SIS (C2) -> discard to DW96W at C3 X2
		position(row,2,position = OffsetDict[offset])
		aspirate(300,depth=90,speed=50, mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(300, depth=96, speed=50)
		position(row,2,position = OffsetDict[offset])
		aspirate(250,depth=92,speed=50, mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(250, depth=87, speed=50)
			
		# pick up 2 x 250ul of Tween20 from C4, add to C2
		position(row,4,position = OffsetDict[offset])
		aspirate(250,depth=96,speed=40, mix=0)
		position(row,2,position = OffsetDict[offset])
		dispense(250, depth=96, speed=90)

		position(row,4,position = OffsetDict[offset])
		aspirate(250,depth=96,speed=40, mix=0)
		position(row,2,position = OffsetDict[offset])
		dispense(250, depth=85, speed=90)
		
		# discard tips
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

