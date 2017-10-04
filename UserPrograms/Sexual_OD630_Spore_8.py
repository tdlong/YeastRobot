import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  BLANK  DW24P  DW24P  BLANK  SW96P  SW96P  
SW24P  SW24P  BLANK  DW24P  DW24P  BLANK  SW96P  SW96P 
SW24P  SW24P  BLANK  DW24P  DW24P  BLANK  BLANK  BLANK
SW24P  SW24P  BLANK  DW24P  DW24P  BLANK  BLANK  BLANK
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
CurrentTipPosition = 1																	

for col in [2,3]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,col)
		mix(300,90,100,5)
		
		# from SW24 to SW96 empty
		position(row,col)
		aspirate(myvol,depth=80,speed=50, mix=3)		
		position(col-2,8,position = OffsetDict[row])
		dispense(myvol, depth=50, speed=50)

		# from SW24 to SW96 empty
		position(row,col)
		aspirate(myvol,depth=80,speed=50, mix=3)
		position(col-2,9,position = OffsetDict[row])
		dispense(myvol, depth=50, speed=50)

		# from SW24 to DW24  X4
		for i in [1,2,3,4]:
			position(row,col)
			aspirate(myvol*2.35,depth=95,speed=50, mix=0)
			position(row,col+3,position = OffsetDict[row])
			dispense(myvol*2.35, depth=95, speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

