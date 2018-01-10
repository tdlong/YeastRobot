import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  DW96W  BLANK  BLANK  DW24P  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  DW24P  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  DW24P  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  DW24P  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

myvol = 330
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [6]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# from DW96 @ col 2 to DW24
		position(col-6,2,OffsetDict[row])
		mix(myvol,70,25,5)
		time.sleep(3)     # wait 3 seconds
		position(col-6,2,OffsetDict[row])
		aspirate(myvol,depth=70,speed=25, mix=0)		
		position(row,col)
		dispense(myvol,depth=95, speed=50)

		# get 330ul from DW96 wide @ col 3 to DW96P at col 2
		position(col-6,3,OffsetDict[row])
		aspirate(myvol,depth=95,speed=50, mix=0)	
		position(col-6,2,OffsetDict[row])
		dispense(myvol,depth=70,speed=50)
		
		# from DW96 @ col 2 to DW24
		position(col-6,2,OffsetDict[row])
		mix(myvol,70,25,5)
		time.sleep(3)     # wait 3 seconds
		position(col-6,2,OffsetDict[row])
		aspirate(myvol,depth=70,speed=25, mix=0)		
		position(row,col)
		dispense(myvol,depth=90, speed=50)

		# 2nd round of 330ul
		# get 330ul from DW96 wide @ col 3 to DW96P at col 2
		position(col-6,3,OffsetDict[row])
		aspirate(myvol,depth=95,speed=50, mix=0)	
		position(col-6,2,OffsetDict[row])
		dispense(myvol,depth=70,speed=50)
		
		# from DW96 @ col 2 to DW24
		position(col-6,2,OffsetDict[row])
		mix(myvol,70,25,5)
		time.sleep(3)     # wait 3 seconds
		position(col-6,2,OffsetDict[row])
		aspirate(myvol,depth=70,speed=25, mix=0)		
		position(row,col)
		dispense(myvol,depth=90, speed=50)

		# dispose tips
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

