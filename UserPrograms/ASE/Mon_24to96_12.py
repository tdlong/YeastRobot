import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  BLANK  DW96P
DW24P  DW24P  DW24P  BLANK  DW96P
DW24P  DW24P  DW24P  BLANK  DW96P
DW24P  DW24P  DW24P  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

# Assume there is a Pellet PLUS 500 ul of SIS solution in each well
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1

for col in [2,3,4]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,col)
		mix(300,99,100,10)

		# 2 * 250 being careful of beads preloaded in 96 well plate
		# from DW24 to DW96 loaded with beads
		position(row,col)
		aspirate(250, depth=99,speed=50, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(250, depth=80, speed=50)
		position(row,col)
		aspirate(250, depth=99,speed=50, mix=0)
		position(col-2,6,position = OffsetDict[row])
		dispense(250, depth=60, speed=50)
					
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

