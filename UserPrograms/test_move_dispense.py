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

myvol = 140
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

# From SW24 to SW96 with 140ul of glycerol
position(0,2)
aspirate(myvol,depth=90,speed=50, mix=3)
position(2,9,position = OffsetDict[2])     # so I can easily see
	
moveDispense(myvol, startdepth = 95, enddepth=60, speed = 50)
		
position(0,0)
ShutDownRobot()
quit()

