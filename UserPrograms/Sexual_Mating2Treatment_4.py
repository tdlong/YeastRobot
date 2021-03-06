import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  SW24P  SW24P  SW24P  SW24P
DW24P  DW24P  DW24P  DW24P  SW24P  SW24P  SW24P  SW24P
DW24P  DW24P  DW24P  DW24P  SW24P  SW24P  SW24P  SW24P
DW24P  DW24P  DW24P  DW24P  SW24P  SW24P  SW24P  SW24P
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

for col in [2,3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,col)
		mix(330,97,100,5)

		# from DW24 to SW24
		position(row,col)
		aspirate(140, depth=98, speed=50, mix=0)
		position(row,col+4)
		dispense(140, depth=90, speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

