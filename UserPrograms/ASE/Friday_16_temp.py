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
CurrentTipPosition = 2																	
CurrentTipPosition = retrieveTips(CurrentTipPosition)
extraSeatTips()

for row in [3]:
	if row in [0,1]:
		adjusted_depth = 92 + row
	elif row == 2:
		adjusted_depth = 94 + row
	else:
		adjusted_depth = 97 + row
	for col in [2,5]:
		# initial mix
		position(row,col)
		mix(300,adjusted_depth + 4,100,3)
manualDisposeTips()
position(0,0)
ShutDownRobot()
quit()

