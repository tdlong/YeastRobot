import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  DW96W  DW96W  DW96P
DW24P  DW24P  DW24P  BLANK  BLANK  BLANK  BLANK
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

for col in [2]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 95 + row*2
		# initial mix
		position(row,col)
		mix(320,adjusted_depth,100,3)					
manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

