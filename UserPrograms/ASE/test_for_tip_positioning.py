import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW96P SW96P SW96P SW96P SW96P SW96P SW96P
SW96P SW96P SW96P SW96P SW96P SW96P SW96P
SW96P SW96P SW96P SW96P SW96P SW96P SW96P
SW96P SW96P SW96P SW96P SW96P SW96P SW96P
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
CurrentTipPosition = 4																	

CurrentTipPosition = retrieveTips(CurrentTipPosition)

for col in [3,4,5,6,7,8,9]
	for row in [0,3]:		
		position(row,col, position = OffsetDict[3])
		mix(100,50,100,1)
		
CurrentTipPosition
		
position(0,0)
ShutDownRobot()
quit()

