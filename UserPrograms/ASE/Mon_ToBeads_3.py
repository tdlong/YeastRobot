import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  DW96P  DW96W  DW96W  BLANK
DW96P  DW96P  DW96W  DW96W  BLANK
DW96P  DW96P  DW96W  DW96W  BLANK
BLANK  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
# This takes ~36m to run in total
##################################

# Assume there is a Pellet in each well
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for row in [0,1,2]:
	for offset in [0,1,2,3]:
		#get tips
		CurrentTipPosition = retrieveTips(CurrentTipPosition)

		#aspirate 2 x 250 ul of Tween20 (C2) -> discard to DW96W at C4 X2
		position(row,2,position = OffsetDict[offset])
		aspirate(300,depth=90,speed=50, mix=0)
		position(row,4, position = OffsetDict[offset])
		dispense(300, depth=80, speed=50)
		position(row,2,position = OffsetDict[offset])
		aspirate(250,depth=92,speed=50, mix=0)
		position(row,4, position = OffsetDict[offset])
		dispense(250, depth=70, speed=50)

		# pick up 2 * 200ul of SDS from C5, add to C2
		position(row,5,position = OffsetDict[offset])
		aspirate(200,depth=97,speed=50, mix=0)
		position(row,2,position = OffsetDict[offset])
		dispense(200, depth=99, speed=100)

		position(row,5,position = OffsetDict[offset])
		aspirate(200,depth=99,speed=50, mix=0)
		position(row,2,position = OffsetDict[offset])
		dispense(200, depth=85, speed=100)
		
		# initial mix
		position(row,2,position = OffsetDict[offset])
		mix(300,90,100,5)

		# 2 * 200 being careful of beads preloaded in 96 well plate
		# from DW96 to DW96 loaded with beads
		position(row,2,position = OffsetDict[offset])
		aspirate(200, depth=95,speed=50, mix=0)
		position(row,3,position = OffsetDict[offset])
		dispense(200, depth=65, speed=50)
		
		position(row,2,position = OffsetDict[offset])
		mix(300,99,100,5)
		
		position(row,2,position = OffsetDict[offset])
		aspirate(200, depth=99,speed=50, mix=0)
		position(row,3,position = OffsetDict[offset])
		dispense(200, depth=55, speed=50)
					
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

