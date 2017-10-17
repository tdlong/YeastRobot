import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P
SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P
SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P
SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P  SW96P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

#  384 ml total dispense -- how much does a resevoir hold (250 ml ...)

CurrentTipPosition = 1																
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

for row in [0,1,2,3]:
	for col in [2,3,4,5,6,7,8]:
		position(row,col,'UL')																		
		testplate()														

home_velmex()
home_EZ()
ShutDownRobot()
