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

counter = 0
for tip in [4,8,12,16]:
	counter += 1
	CurrentTipPosition = tip

	CurrentTipPosition = retrieveTips(CurrentTipPosition)
	extraSeatTips()
			
	myexit='n'
	while myexit=='n':
		position(tip-tip+counter-1,2,position = OffsetDict[3])
		aspirate(250,depth=99,speed=50, mix=0)
		position(tip-tip+counter-1,3,position = OffsetDict[3])
		myexit = raw_input('enter y to exit')
		dispense(250,depth=99,speed=50)
	disposeTips()	

position(0,0)
ShutDownRobot()
quit()

