import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
RES41	SW24P  SW24P  SW24P  SW24P  RES41
RES41	SW24P  SW24P  SW24P  SW24P
RES41	SW24P  SW24P  SW24P  SW24P
RES41	SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()		# initialize motors, home, etc.


for row in [1]:
	for col in [3,4,5,6]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
		position(1,2)																		
		aspirate(myvol, 75, 7)				# Aspirate(volume,% to bottom,speed)
		#enterToContinue()
		position(row,col)																		
		dispense(myvol, 95, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		enterToContinue()
		disposeTips()


# CurrentTipPosition = retrieveTips(CurrentTipPosition, align="True") + 3
# disposeTips()



#CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
#CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
#CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
#CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
#CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
#while CurrentTipPosition < 2	CurrentTipPosition = retrieveTips(CurrentTipPosition)
#EZ_GoTo_A(4500, ezSlow)	    # 6800 to 6500 = -2mm ADL Sept 20  to 5500 + 7mm																					#Punch Out Tips
#EZ_GoTo_A(6000, ezSlow)	    # 6800 to 6500 = -2mm ADL Sept 20  to 5500 + 7mm																					#Punch Out Tips

InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
