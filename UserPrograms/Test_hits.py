import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW96P  SW96P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

myvol = 300
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

col=2
for row in [0,1,2,3]:
	CurrentTipPosition = retrieveTips(CurrentTipPosition)
	CurrentTipPosition = CurrentTipPosition + 3
				
	# From SW24P to SW24P with media
	position(row,col)
	aspirate(myvol,depth=80,speed=50,mix=0)
	xx = raw_input("Waiting for drops, hit enter")
	position(row,col)
	dispense(myvol,depth=80,speed=50)
				
	disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

