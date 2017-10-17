import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  SW24P  SW24P  RES41
SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

#  384 ml total dispense -- how much does a resevoir hold (250 ml ...)

CurrentTipPosition = 25																	
myvol = 1000
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

CurrentTipPosition = retrieveTips(CurrentTipPosition)	
for row in [0,1]:
	for col in [2,3,4,5]:
		position(0,6)																		
		aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
		position(row,col)																		
		dispense(myvol, 100, 50)														# Dispense(volume, %to bottom, speed, blowout)

position(0,8)
print("add more YPD")
enterToContinue():

for row in [2,3]:
	for col in [2,3,4,5]:
		position(0,6)																		
		aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
		position(row,col)																		
		dispense(myvol, 100, 50)														# Dispense(volume, %to bottom, speed, blowout)
disposeTips()																						
fast_home_velmex()
ShutDownRobot()
