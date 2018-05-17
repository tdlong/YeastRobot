import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
DW96W  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
DW96W  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
DW96W  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
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

for row in [0,1,2,3]:
	for offset in [0,1,2,3]:

		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,2,position = OffsetDict[offset])
		mix(320,97,100,10)

		# from DW96W to SW24P
		position(row,2,position = OffsetDict[offset])
		aspirate(140, depth=98, speed=50, mix=0)
		position(offset,row+3)
		dispense(140, depth=90, speed=50)


		for i in [7,8]:
            position(row,2)
            aspirate(140,depth=99,speed=50, mix=2)
            position(row, i, position = OffsetDict[offset])
            moveDispense(140, startdepth = 95, enddepth=60, speed = 50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

