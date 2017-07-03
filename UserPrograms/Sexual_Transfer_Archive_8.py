import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
DW24P  DW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
DW24P  DW24P  BLANK  SW24P  SW24P  BLANK  BLANK  BLANK
DW24P  DW24P  BLANK  SW24P  SW24P  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 140
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()

for(col in 2:3):
	for(row in 0:3):
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		# from DW24 to SW24
		position(row,col)
		aspirate(myvol, depth=80, speed=50)
		position(row,col+3)
		dispense(myvol, depth=80, speed=50)
		position(row,col)
		aspirate(2*myvol, depth=80, speed=50)
		position(col-2,8,OffsetDict[row])
		dispense(2*myvol, depth=80, speed=50)
		position(row,col)
		aspirate(myvol, depth=80, speed=50)
		position(col-2,9,OffsetDict[row])
		dispense(myvol, depth=80, speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

