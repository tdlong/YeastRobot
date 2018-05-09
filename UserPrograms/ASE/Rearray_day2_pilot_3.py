import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW96P  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK
DW96W  SW96P  SW96P  SW96P  BLANK  BLANK  BLANK  BLANK
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

for row in [0,1,2]:
        for offset in [0,1,2,3]:
		
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,2, position = OffsetDict[offset])
		mix(300,98,100,5)
		
		# From DW96W to SW96P with 140ul of glycerol
		# 3 replicate glycerol stocks
		for i in [0,1,2,3]:
                    	position(row,2, position = OffsetDict[offset])
                    	aspirate(myvol,depth=99,speed=50, mix=3)
                    	position(i, row + 3, position = OffsetDict[offset])
                    	moveDispense(myvol, startdepth = 95, enddepth=60, speed = 50)
		
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

