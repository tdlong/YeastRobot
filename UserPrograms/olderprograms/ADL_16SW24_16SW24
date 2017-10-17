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
position(1,2)
enterToContinue()

for row in [1]:
	for col in [3,4,5,6]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
		position(1,2)																		
		aspirate(myvol, 75, 7)				# Aspirate(volume,% to bottom,speed)
		position(row,col)																		
		dispense(myvol, 95, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
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
#EZ_GoTo_A(6000, ezSlow)	    # 6800 to 6500 = -2mm ADL Sept 20  to 5500 + 7mm

#16_SW24 to 16_SW24 (20 ul)
deck="""\
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P  SW24P
"""
for row in [0,1,2,3]:
	for col in [2,3,4,5]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(row,col)																		
		aspirate(20, 90, 7)				# Aspirate(volume,% to bottom,speed)
		position(row,col+4)																		
		dispense(20, 90, 7, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()

#4_DW96 to 16_SW24 (20 ul)
deck="""\
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
DW96P  SW24P  SW24P  SW24P  SW24P
"""
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

#4_DW96 to 4_DW96 (500 ul)
deck="""\
DW96P  DW24P
DW96P  DW24P
DW96P  DW24P
DW96P  DW24P
"""
for row in [0,1,2,3]:
	for off in [1,2,3,4]:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(row,2,off)																		
		moveAspirate(500, 20, 70, 20)				# Aspirate(volume,% to bottom,speed)
		position(row,3,off)		
		# def moveDispense(vol, startdepth = 100, speed = 100, blowout = 'N'):
		moveDispense(500, 80, 20, 'Y')			# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()







																					#Punch Out Tips

InitializeRobot()		# initialize motors, home, etc.
ShutDownRobot()
