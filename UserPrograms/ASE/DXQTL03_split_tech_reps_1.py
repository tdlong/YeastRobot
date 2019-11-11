import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  DW24P  BLANK  BLANK
BLANK  DW24P  DW24P  DW24P  DW24P  BLANK  BLANK
BLANK  DW24P  DW24P  DW24P  DW24P  BLANK  BLANK
BLANK  DW24P  DW24P  DW24P  DW24P  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

# Assume there is a Pellet PLUS 1 mL of spo solution in each well
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1
myvol = 100
for col in [3,4,5,6]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth_row = 95 + row*2

		#Transfer 100uL from master DW24P at C2 to treatment DW24P at c3-6
		position(0,2)
		aspirate(myvol, depth=99,speed=100, mix=7)
		position(row,col)
		dispense(myvol, depth=adjusted_depth_row - 10, speed=50)
					
		#disposeTips()
		manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

