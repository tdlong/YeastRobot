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
myvol = 300
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
# read in deck, etc
DefineDeck(deck)
printDeck()

# InitializeRobot(DOEZ=False)
InitializeRobot()

# test movement
#position(0,0)
#position(0,4)
#position(3,4)
#position(3,3)

# plates
#newplate(0,2)
#newplate(0,3)
#newplate(3,0)   # tip eject
# etc

# tips
retrieveTips(1, align="True")
disposeTips()
position(0,3)


# dispose Tips
InitializeRobot()
retrieveTips(1)
position(0,3)
aspirate(200,depth=90,speed=50)
position(0,4)
dispense(200,depth=90,speed=50)
disposeTips()
position(0,0)
ShutDownRobot(DOEZ=False)
