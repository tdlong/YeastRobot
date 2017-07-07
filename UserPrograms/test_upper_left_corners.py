import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK  BLANK
"""
#   2       3       4       5       6       7      8      9
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 300
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
# read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()

# ...Plate(row,column)
disposeTips()
retrieveTips(1)

defineCornersOf24WellPlates(0,3)

position(0,0)
ShutDownRobot(DOEZ=False)
