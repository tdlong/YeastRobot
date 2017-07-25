import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

myvol = 140
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
#  OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPostion = 1

for col in [2,3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix
		position(row,col)
		mix(300,90,100,25)

		position(row,col)
		aspirate(myvol,depth=80,speed=50,mix=3)
		position(row,col+4)
		dispense(myvol,depth=80,speed=50)
		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

