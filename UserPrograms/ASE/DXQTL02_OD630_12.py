import sys
#  where RobotControl.py, etc lives
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  SW96P  SW96P  BLANK  BLANK
DW24P  DW24P  DW24P  DW24P  SW96P  SW96P  BLANK  BLANK
DW24P  DW24P  DW24P  DW24P  SW96P  SW96P  BLANK  BLANK
DW24P  DW24P  DW24P  DW24P  SW96P  SW96P  BLANK  BLANK
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
col_counter = -1

for col in [2,3,4]:
	col_counter += 1
	row_counter = -1	

	for row in [0,1,2,3]:
		
		row_counter += 1
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		extraSeatTips()
		adjusted_depth = 95 + row*2

		# initial mix
		position(row,col)
		mix(300,adjusted_depth,100,10)
		
		# from DW24P to empty SW96P
		position(row,col)
		aspirate(myvol,depth=adjusted_depth,speed=50,mix=3)
		position(row-row_counter+col_counter,6, position = OffsetDict[row])
		dispense(myvol, depth=adjusted_depth-15, speed=50)

		position(row,col)
		aspirate(myvol,depth=adjusted_depth,speed=50,mix=3)
		position(row-row_counter+col_counter,7, position = OffsetDict[row])
		dispense(myvol, depth=adjusted_depth-15, speed=50)
		
		#disposeTips()
		manualDisposeTips()

position(0,0)
ShutDownRobot()
quit()

