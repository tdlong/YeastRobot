import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  DW96W  BLANK BLANK BLANK BLANK BLANK 
DW96W  DW96W  BLANK BLANK BLANK BLANK BLANK 
DW96W  DW96W  BLANK BLANK BLANK BLANK BLANK  
DW96W  DW96W  BLANK BLANK BLANK BLANK BLANK  
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 13


# eventually row in 0,1,2,3

# get tips
CurrentTipPosition = retrieveTips(CurrentTipPosition)
extraSeatTips()
			
# pick up 250ul of selective media from C3, add to C2, mix
myexit='n'
while myexit=='n':
	position(0,2,position = OffsetDict[0])
	aspirate(250,depth=99,speed=50, mix=0)
	position(0,2,position = OffsetDict[0])
	myexit = raw_input('enter y to exit')
	dispense(250,depth=99,speed=50)
		
disposeTips()	
position(0,0)
ShutDownRobot()
quit()

