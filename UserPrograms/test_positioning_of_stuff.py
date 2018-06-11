import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

def nextplatetotest():
	NextOffset = int(raw_input("enter next offset"))
	return NextOffset

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

retrieveTips(1, align="True")
enterToContinue()
disposeTips()
exit="N"
while exit=="N":
	NN = nextplatetotest()
	retrieveTips(NN, align="True")
	exit = raw_input("Exit -> Y, more -> N")

position(0,0)
ShutDownRobot(DOEZ=False)
