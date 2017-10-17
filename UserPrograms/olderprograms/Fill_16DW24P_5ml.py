import sys
#  where RobotControl.py, etc lives
#sys.path.append('/usr/bin/YeastRobotLibrary')
#  /usr/bin/YeastRobotLibrary is a symlink to the current code
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
DW24P  DW24P  DW24P  DW24P  RES41
DW24P  DW24P  DW24P  DW24P
DW24P  DW24P  DW24P  DW24P
DW24P  DW24P  DW24P  DW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

#  1924 ml total dispense -- how much does a reservoir hold (250 ml ...)?  refill every other plate

CurrentTipPosition = 25																	
myvol = 1000
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

CurrentTipPosition = retrieveTips(CurrentTipPosition)	
for row in [0,1]:
	for col in [2,3,4,5]:
		if col%%2 == 0:
			position(0,8)
			print("add more sporulation media")
			enterToContinue():
		for rep in [1,2,3,4,5]:
			position(0,6)																		
			aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
			position(row,col)																		
			dispense(myvol, 100, 50)														# Dispense(volume, %to bottom, speed, blowout)
disposeTips()																						
fast_home_velmex()
ShutDownRobot()
