import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
RES41  SW24P  SW24P  SW24P  SW24P
RES41  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 3																	
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()							# initialize motors, home, etc.

CurrentTipPosition = OLDretrieveTips(CurrentTipPosition)

enterToContinue()	
for row in [1]:
	for col in [3,4,5,6]:
		position(1,2)																		
		aspirate(myvol, 85, 7)				# Aspirate(volume,% to bottom,speed)
		#enterToContinue()
		position(row,col)																		
		dispense(myvol, 95, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		enterToContinue()

disposeTips()
fast_home_velmex()
home_EZ()
																					

