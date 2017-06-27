import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
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
myvol = 200
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
# read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()

#retrieveTips(1, align="True")
CurrentTipPosition = retrieveTips(CurrentTipPosition)
position(0,2,"UL")
aspirate(myvol,depth=90,speed=50)
position(0,3)
dispense(myvol,depth=90,speed=50)
disposeTips()

CurrentTipPosition = retrieveTips(CurrentTipPosition)
position(0,2,"UR")
aspirate(myvol,depth=90,speed=50)
position(0,4)
dispense(myvol,depth=90,speed=50)
disposeTips()

position(0,0)
ShutDownRobot()
quit()

