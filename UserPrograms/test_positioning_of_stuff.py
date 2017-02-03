import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 300
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
# read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot(EZ=False)

# test movement
position(0,0)
position(0,4)
position(3,4)
position(3,3)
position(2,0)
position(0,2)

# plates
new_plate(0,2)
new_plate(0,3)
# etc

# tips
retrieveTips(1, align="True"):
retrieveTips(5, align="True"):
# etc

# liquid disposal (no EZ)
liquidDisposal()

# dispose Tips
disposeTips()

position(0,0)
ShutDownRobot(EZ=False)
