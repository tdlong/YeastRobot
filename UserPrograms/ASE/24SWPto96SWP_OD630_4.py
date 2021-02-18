import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
SW24P  SW96P  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
SW24P  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
SW24P  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
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
CurrentTipPosition = 3																	

for col in [2]:
	for row in [0,1,2,3]:
		
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		if row in [0,1]:
			adjusted_depth24SWP = 91 + row
		elif row == 2:
			adjusted_depth24SWP = 95 + row
		else:
			adjusted_depth24SWP = 97 + row

		# initial mix
		position(row,col)
		mix(300,adjusted_depth24SWP + 4,100,5)

        # From SW24 to SW96 empty for OD
		position(row,col)
		aspirate(myvol,depth=adjusted_depth24SWP + 4,speed=50, mix=3)
		position(0, col + 1, position = OffsetDict[row])
		dispense(myvol, depth=80, speed=50)
		
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

