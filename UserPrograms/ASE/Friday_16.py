import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  SW24P  SW24P  DW24P  DW24P  DW24P  DW24P 
SW24P  SW24P  SW24P  SW24P  DW24P  DW24P  DW24P  DW24P 
SW24P  SW24P  SW24P  SW24P  DW24P  DW24P  DW24P  DW24P 
SW24P  SW24P  SW24P  SW24P  DW24P  DW24P  DW24P  DW24P 
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

myvol = 140
#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
#  read in deck, etc
DefineDeck(deck)
printDeck()
InitializeRobot()
CurrentTipPosition = 1																	

for col in [2,3,4,5]:
	for row in [0,1,2,3]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		if row in [0,1]:
			adjusted_depth24SWP = 91 + row
		elif row == 2:
			adjusted_depth24SWP = 95 + row
		else:
			adjusted_depth24SWP = 97 + row
		
		adjusted_depth96DWPS = 92 + row*2
		
		# initial mix
		position(row,col)
		mix(300,adjusted_depth24SWP + 4,100,5)
		
		# from SW24 to DW24  320 ul X3 = 990ul
		# this is the most we can get from a plate when we start with 1.4ml
		for i in [1,2,3]:
			position(row,col)
			aspirate(320,depth=adjusted_depth24SWP + 4,speed=50, mix=0)
			position(row,col+4,position = OffsetDict[row])
			dispense(320, depth=adjusted_depth96DWPS + 3, speed=50)
		#disposeTips()
		manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

