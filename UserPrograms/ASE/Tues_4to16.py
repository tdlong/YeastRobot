import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
DW96W  SW24P  SW24P  SW24P  SW24P  BLANK  BLANK
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

for row in [0,1,2,3]:
	for offset in [0,1,2,3]:

		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		if row in [0,1]:
			adjusted_depth24SWP = 91 + row
		elif row == 2:
			adjusted_depth24SWP = 95 + row
		else:
			adjusted_depth24SWP = 97 + row
		
		adjusted_depth96DWPS = 96 + row

		# initial mix
		position(row,2,position = OffsetDict[offset])
		mix(320,adjusted_depth96DWPS,100,10)

		# from DW96W to SW24P
		position(row,2,position = OffsetDict[offset])
		aspirate(140, depth=adjusted_depth96DWPS, speed=50, mix=0)
		position(offset,row+3)
		dispense(140, depth=adjusted_depth24SWP + 4, speed=50)
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

