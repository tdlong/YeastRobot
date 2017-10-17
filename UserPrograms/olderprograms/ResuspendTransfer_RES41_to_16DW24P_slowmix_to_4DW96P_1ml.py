import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
RES41 DW24P DW24P DW24P DW24P DW96P BLANK BLANK
BLANK DW24P DW24P DW24P DW24P DW96P BLANK BLANK
BLANK DW24P DW24P DW24P DW24P DW96P BLANK BLANK
BLANK DW24P DW24P DW24P DW24P DW96P BLANK BLANK
"""
# 2     3     4     5     6     7     8     9

#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 1000
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

#PROGRAM 3 OVERVIEW:
#transfer 1 ml of YPER media from reservoir to 24 well plate containing yeast
#Mix solution
#transfer entire 1 ml to DW96P (A1 - A5UL, A2-A5UR...etc.)
#change tips

ResRow=0
ResCol=2
rows = [0, 1, 2, 3]
columnsAndOffsets = [[3, 'UL'], [4, 'UR'], [5, 'LL'], [6, 'LR']]
DesCol = 7

#get tips from tip box A, 'UL'

for i in rows:
	for j in columnsAndOffsets:
		CurrentTipPosition = retrieveTips(CurrentTipPosition)	
		position(ResRow,ResCol)
		aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
		position(i,j[0])
		dispense(myvol,100,50,'Y','MIX&ASPIRATE')
		position(i,DesCol,j[1])																		
		dispense(myvol, 25, 50,'Y')														# Dispense(volume, %to bottom, speed, blowout)
		disposeTips()
fast_home_velmex()
ShutDownRobot()
