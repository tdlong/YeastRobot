import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
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



CurrentTipPosition = 1										#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)											# read in deck		
															# define first tip offset
															# check plates, etc. -> output deck back to user
printDeck()
InitializeRobot()											# initialize motors, home, etc.
row = 0
for col in [3,4,5,6]:
	CurrentTipPosition = retrieveTips(CurrentTipPosition)	# automatically gets next box/offset with tips
															# when all 6 boxes are empty, arm moves to side and asks user for more tips!
	position(row,2,OffsetDict[col-2])    					# Goto(x,y,offset)
	moveAspirate(myvol, 35, 80, 50)							# Aspirate(volume,start % to bottom,end % to bottom, speed)
															# after Aspirate return to safe height
	position(row,col)										# it knows the "offset" because it is a 24 well plate
	dispense(myvol, 100, 50,'Y')							# Dispense(volume, %to bottom, speed)
#	moveDispense(myvol, 50, 50,'Y')							# Dispense(volume, %to bottom, speed)
															# return to safe height
	liquidDisposal()							    		# smart enough to goto liquid Waste and dispense the remain 50ul
	disposeTips()											# again smart enough to do this

fast_home_velmex()
ShutDownRobot()
