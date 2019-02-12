import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################


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
		adjusted_depth = 96 + row
		
		# initial mix
		position(row,2, position = OffsetDict[offset])
		mix(320,adjusted_depth + 1,100,10)
		
		# from DW96 to SW96
		position(row,2, position = OffsetDict[offset])
		aspirate(140,depth=adjusted_depth,speed=50,mix=0)
		position(row,3, position = OffsetDict[offset])
		moveDispense(140, startdepth = 95, enddepth=60, speed = 50)
		
		position(row,2, position = OffsetDict[offset])
		aspirate(140,depth=adjusted_depth,speed=50,mix=2)
		position(row,4, position = OffsetDict[offset])
		moveDispense(140, startdepth = 95, enddepth=60, speed = 50)
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

