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

myvol = 300
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

for row in [0,1,2,3]:
    for offset in [0,1,2,3]:
		
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 97 + row
		
		#aspirate 300 ul of H2O (C3) -> discard to DW96W at C4
		position(row,3, position = OffsetDict[offset])
		aspirate(myvol,depth=adjusted_depth - 2,speed=50,mix=0)
		position(row,4, position = OffsetDict[offset])
		dispense(myvol, depth=adjusted_depth-1, speed=50)

		#transfer 3x320 ul of YPDa(C6) -> resuspend pellet (C3)
		position(row,6, position = OffsetDict[offset])
		aspirate(320,depth=adjusted_depth-1,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(320, depth=adjusted_depth-1, speed=50)

		position(row,6, position = OffsetDict[offset])
		aspirate(320,depth=adjusted_depth-1,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(320, depth=adjusted_depth - 10, speed=50)

		position(row,6, position = OffsetDict[offset])
		aspirate(320,depth=adjusted_depth-1,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		dispense(320, depth=adjusted_depth - 15, speed=50)

		mix(300,adjusted_depth - 1,100,5)
		
		#disposeTips()
		manualDisposeTips()
		
position(0,0)
ShutDownRobot()
quit()

