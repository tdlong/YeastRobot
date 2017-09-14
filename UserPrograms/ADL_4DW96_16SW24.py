import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
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
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.
position(1,2)
enterToContinue()

#4_DW96 to 16_SW24 (20 ul)
for row in [0,1,2,3]:
	for col in [3,4,5,6]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(row,2,OffsetDict[col-2])																		
		# def moveAspirate(vol, startdepth = 100, enddepth = 100, speed = 100)
		# 0 = top and 100 = bottom
		moveAspirate(20,20,30,20)
		position(row,col)																		
		dispense(20, 90, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()

InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
