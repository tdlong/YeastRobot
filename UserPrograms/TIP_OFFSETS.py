import sys
#  where RobotControl.py, etc lives
#sys.path.append('/path/to/application/app/folder')
from RobotControl import *

#################################
###  Define Deck Layout
#################################
deck="""\
SW24P  SW24P  SW24P  SW24P  RES41
SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
SW24P  SW24P  SW24P  SW24P
"""
#   2       3       4       5       6
#   note the 1st user defined column is "2" not zero or one, since tips are at 0 & 1
##################################

CurrentTipPosition = 1																	
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)																				
printDeck()
InitializeRobot()																				# initialize motors, home, etc.

CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
CurrentTipPosition = retrieveTips(CurrentTipPosition) + 3
disposeTips()																						
home_velmex()
home_EZ()
ShutDownRobot()
