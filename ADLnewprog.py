import sys
#  where RobotControl.py, etc lives
sys.path.append('/path/to/application/app/folder’)
from RobotControl import *


#################################
###  Define Deck Layout
#################################
deck="""\
DW96P	SW24P	SW24P	SW24P	SW24P
DW96P	SW24P	SW24P	SW24P	SW24P
DW96P	SW24P	SW24P	SW24P	SW24P
DW96P	SW24P	SW24P	SW24P	SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	#  1 = UL of BoxA, 2 = UR of BoxA, 3 = LL of BoxA, etc.
myvol = 100
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}

DefineDeck(deck)																				# read in deck		
																												# define first tip offset
																												# check plates, etc. -> output deck back to user
PrintDeck()
InitializeRobot()																				# initialize motors, home, etc.

for row in [0,1,2,3]:
	for col in range(3,4,5,6):
		retrieveTips()																			# automatically gets next box/offset with tips
																												# when all 6 boxes are empty, arm moves to side and asks user for more tips!
		position(row,2,OffsetDict[col-2])    								# Goto(x,y,offset)
		aspirate(myvol, 100)							   								# Aspirate(volume,% to bottom,speed)
																												# after Aspirate return to safe height
		position(row,col)																		# it knows the "offset" because it is a 24 well plate
		dispense(myvol, 100)																# Dispense(volume, %to bottom, speed)
																												# return to safe height
		liquidDisposal()							    									# smart enough to goto liquid Waste and dispense the remain 50ul
		disposeTips()																				# again smart enough to do this

ShutDownRobot()
		

####################################
TBOXA TBOXB DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
TBOXC TBOXD DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
TBOXE TBOXF DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
LWSTE TDISP DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK

#PROGRAM OVERVIEW: Transfer 50 ul from DW96P to SW24P and change tips each time
