import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
SW24P SW24P SW24P SW24P DW96P BLANK BLANK BLANK
SW24P SW24P SW24P SW24P DW96P BLANK BLANK BLANK
SW24P SW24P SW24P SW24P DW96P BLANK BLANK BLANK
SW24P SW24P SW24P SW24P DW96P BLANK BLANK BLANK
"""
# 2     3     4     5     6     7     8     9

#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 25																	
myvol = 500
DefineDeck(deck)																				
printDeck()
InitializeRobot()		


#PROGRAM 3 OVERVIEW - transfer 1 ml of glycerol stock from 16 SW24P to 4 DW96P. New tips each time.

rows = [0, 1, 2, 3]
DesCol = 6
#Each list element in the columnAndOffsets list corresponds to the column to be aspirated from and the 96-plate well offset in which to dispense
columnsAndOffsets = [[2, 'UL'], [3, 'UR'], [4, 'LL'], [5, 'LR']]
#use tipBoxGenerator() to generate a tip box location that still has tips


for i in rows:
	for j in columnsAndOffsets:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)
		position(i, j[0])
		aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
		position(i, DesCol, j[1])
		dispense(myvol, 50, 50,'Y','MIX')		#50 percent down to avoid liquid overflow						# Dispense(volume, %to bottom, speed, blowout)
		#mix(myvol)
		disposeTips()
fast_home_velmex()
ShutDownRobot()
