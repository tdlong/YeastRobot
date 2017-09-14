import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
DW96P SW24P SW24P SW24P SW24P BLANK BLANK BLANK
"""
# 2     3     4     5     6     7     8     9

#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 25		
myvol = 50															
DefineDeck(deck)																				
printDeck()
InitializeRobot()		

#PROGRAM OVERVIEW: Transfer 50 ul from DW96P to SW24P and change tips each time

rows = [0,1,2,3]
#source column (column of 96 well plates)
SrcCol = 2
#ORDERED destination columns and offsets
DesCols = [[3, 'UL'], [4, 'UR'], [5, 'LL'], [6, 'LR']]


for i in rows:
	for j in DesCols:
		#Get tips
		CurrentTipPosition = retrieveTips(CurrentTipPosition)	
		#Go to source plate
		position(i, SrcCol, j[1])
		#aspirate 50 uL at current position
		aspirate(myvol, 100, 100)
		#go to destination plate
		position(i, j[0])
		#dispense 50 uL at current position
		dispense(myvol, 100, 100, 'Y')
		#Dispose tips
		disposeTips()	
