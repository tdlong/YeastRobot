import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
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

for row in [0]:
	for offset in [0,1,2,3]:

		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 96 + row
		adjusted_depth2 = 98 + offset

		# from DW96W to SW24P
		position(offset,row+3)
		aspirate(140, depth=adjusted_depth2, speed=50, mix = 5)
		dispense(140, depth=adjusted_depth2, speed=50)
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

