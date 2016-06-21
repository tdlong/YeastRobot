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



CurrentTipPosition = 25
myvol = 500
OffsetDict={1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
DefineDeck(deck)											
printDeck()
InitializeRobot()											
CurrentTipPosition = retrieveTips(CurrentTipPosition)
position(0,2,'UL') 
checkAlignment()  					
disposeTips()											
fast_home_velmex()
ShutDownRobot()
