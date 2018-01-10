import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW24P  SW24P  SW24P  SW24P
DW96W  SW24P  SW24P  SW24P  SW24P
DW96W  SW24P  SW24P  SW24P  SW24P
DW96W  SW24P  SW24P  SW24P  SW24P
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

for offset in [0,1,2,3]:
	for row in [0]:                   # change to [0,1,2,3] for 4 plates
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		
		# initial mix and aspirate for DW96 at C2
		position(row,2,position = OffsetDict[offset])
		mix(330,98,100,5)
		aspirate(100, depth=98, speed=50, mix=0)

		# dispense to SW24 plate at C3 (offset 0), C4 (offset 1), etc.
		position(offset,3 + row)
		dispense(100, depth=96, speed=50)

		disposeTips()
		
position(0,0)
ShutDownRobot()
quit()

