import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  DW96W  BLANK  BLANK  DW24P  DW24P  DW24P  DW24P
DW96P  DW96W  BLANK  BLANK  DW24P  DW24P  DW24P  DW24P
DW96P  DW96W  BLANK  BLANK  DW24P  DW24P  DW24P  DW24P
DW96P  DW96W  BLANK  BLANK  DW24P  DW24P  DW24P  DW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 330
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()

for col in [6,7,8,9]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		# from DW96 to DW24
		position(col-6,2,OffsetDict[row])
		moveAspirate(myvol, startdepth=20, enddepth=40, speed=50)
		position(row,col)
		dispense(myvol,depth=80, speed=50)
		for i in [0,1]:
			position(col-6,3,OffsetDict[row])
			moveAspirate(myvol, startdepth=(50 + (i*10)), enddepth=(80 + (i*10)), speed=50)
			position(col-6,2,OffsetDict[row])
			moveDispense(myvol,startdepth=50, enddepth=80, speed=50)
			time.sleep(3)     # wait 3 seconds
			position(col-6,2,OffsetDict[row])
			moveAspirate(myvol, startdepth=20, enddepth=40, speed=50)
			position(row,col)
			dispense(myvol,depth=80, speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

