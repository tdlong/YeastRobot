import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  BLANK  BLANK  SW24P  BLANK  BLANK  SW96P  SW96P
DW24P  BLANK  BLANK  SW24P  BLANK  BLANK  BLANK  BLANK
DW24P  BLANK  BLANK  SW24P  BLANK  BLANK  BLANK  BLANK
DW24P  BLANK  BLANK  SW24P  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

myvol = 140
myAdepth = 90
myDdepth = 80
my96depth = 50
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [2]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,col)
		mix(300,myAdepth,100,5)

		# from DW24 to SW24
		position(row,col)
		aspirate(myvol, depth=myAdepth, speed=50, mix=3)
		position(row,col+3)
		dispense(myvol, depth=myDdepth, speed=50)
		
		# OD630 1
		position(row,col)
		aspirate(myvol, depth=myAdepth, speed=50, mix=3)
		position(col-2,8,OffsetDict[row])
		dispense(myvol, depth=75, speed=50)
		
		# OD630 2
		position(row,col)
		aspirate(myvol, depth=myAdepth, speed=50, mix=3)
		position(col-2,9,OffsetDict[row])
		dispense(myvol, depth=75, speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

