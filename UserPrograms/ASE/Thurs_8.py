import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
SW24P  SW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
SW24P  SW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
SW24P  SW24P  BLANK  SW24P  SW24P  BLANK  SW96P  SW96P
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
		extraSeatTips()
		adjusted_depth = 92 + row*2

		# initial mix
		position(row,col)
		mix(300,90,100,5)
		
		# from SW24 to SW24 with media
		position(row,col)
		aspirate(myvol,depth=adjusted_depth + 5,speed=50,mix=0)
		position(row,col+3)
		dispense(myvol, depth=90, speed=50)
				
		# col 2 of 24 well plate maps to col 8
		# col 3 of 24 well plate maps to col 9
		# the 96 well plate rows are just replicates
		# row zero is for OD, rows 1-3 are glycerol stock

        # From SW24 to SW96 empty for OD
		position(row,col)
		aspirate(myvol,depth=adjusted_depth + 2,speed=50, mix=3)
		position(0, col + 6, position = OffsetDict[row])
		dispense(myvol, depth=80, speed=50)
		
		# From SW24 to SW96 with 140ul of glycerol
		# 3 replicate glycerol stocks
		for i in [1,2,3]:
                        position(row,col)
                        aspirate(myvol,depth=adjusted_depth + 2,speed=50, mix=3)
                        position(i, col + 6, position = OffsetDict[row])
                        moveDispense(myvol, startdepth = 95, enddepth=60, speed = 50)
		
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

