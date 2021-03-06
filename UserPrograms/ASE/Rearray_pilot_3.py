import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW96P  DW96W  DW96W  DW96W  DW96W  BLANK  BLANK  BLANK
SW96P  DW96W  DW96W  DW96W  DW96W  BLANK  BLANK  BLANK
SW96P  DW96W  DW96W  DW96W  DW96W  BLANK  BLANK  BLANK
SW96P  DW96W  DW96W  DW96W  DW96W  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################																

myvol = 100
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

for row in [0,1,2]:
        for offset in [0,1,2,3]:
		
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()

		# from SW96 to DW96
		position(row,2, position = OffsetDict[offset])
		aspirate(myvol,depth=80,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(myvol, depth=75, speed=50)
		
		# initial mix
		position(row,2, position = OffsetDict[offset])
		mix(100,96,100,5)
		
		# from SW96 to DW96
		position(row,2, position = OffsetDict[offset])
		aspirate(myvol,depth=96,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(myvol, depth=75, speed=50)
		
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()