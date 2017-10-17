import sys
sys.path.append('/home/pi/Desktop/ADL/YeastRobot/PythonLibrary')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
SW24P SW24P SW24P SW24P SW24P SW24P SW24P SW24P
SW24P SW24P SW24P SW24P SW24P SW24P SW24P SW24P
SW24P SW24P SW24P SW24P SW24P SW24P SW24P SW24P
SW24P SW24P SW24P SW24P SW24P SW24P SW24P SW24P
"""
# 2     3     4     5     6     7     8     9

#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1#25																	
myvol = 500
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

#PROGRAM 2 OVERVIEW - transfer 10 ul (0.01ml) from 16 SW24P to another set of 16. Cover piercing may be required.  

rows = [0, 1, 2, 3]
columns = [2, 3, 4, 5]

#get tips from tip box A, 'UL'

CurrentTipPosition = retrieveTips(CurrentTipPosition)	
for i in rows:
	for j in columns:
		position(i, j)
		aspirate(myvol, 100, 50)							   						# Aspirate(volume,% to bottom,speed)
		position(i,j+4)																		
		dispense(myvol, 90, 50,'Y')														# Dispense(volume, %to bottom, speed, blowout)
		#disposeTips()
fast_home_velmex()
ShutDownRobot()
