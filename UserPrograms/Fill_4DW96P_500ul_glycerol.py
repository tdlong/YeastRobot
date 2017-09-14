import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
DW96P  RES41
DW96P
DW96P
DW96P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

#PROGRAM 1C OVERVIEW - Fill 4 DW96P with glycerol media - 0.5ml each well. Keep tips out of DW96P - no need to change tips. 
#SLOWER ASPIRATE AND DISPENSING SPEED SINCE GLYCEROL IS VISCOUS


#  192 ml total dispense -- how much does a reservoir hold (250 ml ...)?  no refill needed

CurrentTipPosition = 25																	
myvol = 500
OffsetDict={0: 'UL', 1: 'UR', 2: 'LL', 3: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

CurrentTipPosition = retrieveTips(CurrentTipPosition)	
for row in [0,1,2,3]:
	for offset in ['UL','UR','LL','LR']:
		position(0,3)																		
		aspirate(myvol, 100, 25)							   			     	# Aspirate(volume,% to bottom,speed)
		position(row,2,offset)																		
		dispense(myvol, 50, 25,'Y')	#50% down to avoid liquid overflow      Dispense(volume, %to bottom, speed, blowout)

disposeTips()																						
fast_home_velmex()
ShutDownRobot()

