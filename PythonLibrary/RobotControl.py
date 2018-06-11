from __future__ import print_function
import Settings as s
import CellClass as C #cell object definition
import Exceptions as e #exception class definitions for catching excptions
import time #for pauses
import serial #for communicating to controllers through serial ports
import os #for file and directory reading
import threading #for coordinating control between two controllers
from multiprocessing import Process #for coordinating control between two controllers
import sys #for emergency terminate
import traceback #for exception reporting
import select
import subprocess

version = s.version #this string is displayed in text UI, please update in settings.py as you go

######################################################
############GLOBAL DEFINITIONS AND SETTINGS###########
######################################################
'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
VLMXserialPort = s.VLMXserialPort
EZserialPort = s.EZserialPort
EZ=''
velmex=''

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#Define Motors - string assignment 
XMotor = '1'
YMotor = '3' 
ZMotor = '2' 

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#Set Speeds - string assignemnt for MOTOR SPEED value
XSpeedFast = s.XSpeedFast 
YSpeedFast = s.YSpeedFast 
ZSpeedFast = s.ZSpeedFast
XSpeedSlowP = s.XSpeedSlowP
YSpeedSlowP = s.YSpeedSlowP
ZSpeedSlowP = s.ZSpeedSlowP
XSpeedSlow = s.XSpeedSlow
YSpeedSlow = s.YSpeedSlow
ZSpeedSlow = s.ZSpeedSlow
ZSpeedPipet = s.ZSpeedPipet
ezSlow = s.ezSlow
ezFast = s.ezFast

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#Determine number of rows, cols
deck_rows = s.deck_rows
deck_cols = s.deck_cols

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#File Reading
targetDir = s.targetDir

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#Air buffer
airBuffer = s.airBuffer

'''---> EDIT SETTINGS IN SETTINGS.PY, NOT HERE!!<--- '''
#pipetting step conversion
stepsPerUL = s.stepsPerUL
maxUL = s.maxUL

################Runtime Variables (dynamically updated/accessed)####################

#Index tracking, current location
currentx = 0
currenty = 0
currentDisplacement = 0 #Current Plunger Position

#List of lists of cell/plate objects for functional purposes
matrix = [ [],[],[],[] ]

#List of lists of cell/plate type names for UI purposes
DeckLayout = [[],[],[],[]]

#Deck Layout Options
DeckLayoutIndex = dict()

#depth when the plunger is at the very bottom of the syringe
plungerLimit = s.plungerLimit

#detailed output - toggle on/off
verbose = False #true if you want to print out every single command that is sent

#######################################################################################
#######################################################################################
#######################################################################################
################################# FUNCTION DEFINITIONS ################################
#######################################################################################
#######################################################################################
#######################################################################################

			
#############################################################################
##################### INITIAL CONFIGURATION FUNCTIONS #######################
#############################################################################

def initializeVelmexSerial():
	print("			 Initializing Serial Objects")
	#Setup Controller Communication
	BR = s.BR #serial baud rate
	global velmex
	global VLMXserialPort
	#Create and initialize Velmex control object
	try:
		velmex = serial.Serial(port= VLMXserialPort, baudrate = BR, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
	except:
		print('YEASTBOT ERROR: SERIAL PORTS ARE NOT ACCESSIBLE. PLEASE CHECK CONNECTIONS AND TRY AGAIN')
		print(' terminating...')
		terminate()

def initializeEZSerial():
	print("			 Initializing Serial Objects")
	#Setup Controller Communication
	BR = s.BR #serial baud rate
	global EZ
	global EZserialPort
	#Create and initialize Velmex control object
	try:
		EZ = serial.Serial(port= EZserialPort, baudrate=BR, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,timeout=2)
	except:
		print('YEASTBOT ERROR: SERIAL PORTS ARE NOT ACCESSIBLE. PLEASE CHECK CONNECTIONS AND TRY AGAIN')
		print(' terminating...')
		terminate()


def plateCheck(plate):
	if (plate not in C.plateInfo.keys()):
		print('')
		print('       -->ERROR! Selected program has failed deck verification.')
		print('       Revise to ensure all deck items are valid names')
		print('       System will now shut down for safety.')
		print('')
		ShutDownRobot()
	else:
		pass
		
def InitializeRobot(DOvelmex=True, DOEZ=True):
	print('Starting up...\n')
	print('Warning: If motor controller power has been interrupted')
	print('  prior to this run, it is important to home the')
	print('  motors. Failure to do so will result in posit-')
	print('  -ing inaccuracies and plate crashes.\n')
	print('Running motor initialization sequence.')
	print('')
	if(DOvelmex):
		initializeVelmexSerial()
		velmex.close()
		velmex.open()
		home_Velmex()
	if(DOEZ):
		initializeEZSerial()
		EZ.close()
		EZ.open()
		home_EZ()
	loadTips()
	return
			
def printDeck():
	print('')
	print('')
	print('\n\n############### Deck Layout #####################')
	print('0       1       2       3       4       5       6       7       8       9')
	for i in [0,1,2,3]:
		for j in DeckLayout[i]:
			print(j,'  ',end='')
		print()
	print('\n\n')
	myanswer = raw_input('Is this the correct deck layout (y/n)')
	if (myanswer != 'y'):
		print('You did not indicate the correct deck layout')
		exit(1)

def DefineDeck(deck): #assigns plate to each position, sets up objects for each cell/plate
	global matrix
	global DeckLayout
	fixed = [['TBOXA','TBOXB'],['TBOXC','TBOXD'],['TBOXE','TBOXF'],['TDISP','LWSTE']] 
	Deck = deck.split('\n')
	for i in [0,1,2,3]:
		rDeck = fixed[i]+ Deck[i].split()
		cc = 0
		for j in rDeck:
			plateCheck(j)
			matrix[i].append(C.Cell(j,i,cc))
			DeckLayout[i].append(j)	
			cc = cc + 1	

	print('')
	print('--------------------------------------------------------------------------------')
	print('')
	print('        Deck layout has been successfully configured.')
	print('')
	print('--------------------------------------------------------------------------------')
	print('')	 

############################ HOMING FUNCTIONS ###############################

def home_Velmex():

	setVelmexToOnlineMode()
	
	#Go to Home Position (Slow)
	#Clear, index to negative limit, set speed to 200steps/sec, zero motor position, run
	
	#Initialize to fast speed (vlmx)
	VLMX_SetSpeed(XMotor, XSpeedSlowP)
	VLMX_SetSpeed(YMotor, YSpeedSlowP)
	VLMX_SetSpeed(ZMotor, ZSpeedSlowP)

	SendToVelmex('C, I' + ZMotor + 'M-0, I' + ZMotor + 'M' + str(ZSpeedSlow) + ', IA' + ZMotor + 'M-0, R')
	SendToVelmex('C, I' + YMotor + 'M-0, I' + YMotor + 'M' + str(YSpeedSlow) + ', IA' + YMotor + 'M-0, R')
	SendToVelmex('C, I' + XMotor + 'M-0, I' + XMotor + 'M' + str(XSpeedSlow) + ', IA' + XMotor + 'M-0, R')
	
	#Initialize to fast speed (vlmx)
	VLMX_SetSpeed(XMotor, XSpeedSlow)
	VLMX_SetSpeed(YMotor, YSpeedSlow)
	VLMX_SetSpeed(ZMotor, ZSpeedSlow)

	#Go to Home Position (Slow)
	#Clear, index to negative limit, set speed to 200steps/sec, zero motor position, run
	SendToVelmex('C, I' + ZMotor + 'M-0, I' + ZMotor + 'M' + str(ZSpeedSlow) + ', IA' + ZMotor + 'M-0, R')
	SendToVelmex('C, I' + YMotor + 'M-0, I' + YMotor + 'M' + str(YSpeedSlow) + ', IA' + YMotor + 'M-0, R')
	SendToVelmex('C, I' + XMotor + 'M-0, I' + XMotor + 'M' + str(XSpeedSlow) + ', IA' + XMotor + 'M-0, R')
	
	#Initialize to fast speed (vlmx)
	VLMX_SetSpeed(XMotor, XSpeedFast)
	VLMX_SetSpeed(YMotor, YSpeedFast)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)

	print('--------------------------------------------------------------------------------')
	print('')
	print('	 VLMX: INTIALIZING/HOMING COMPLETE')
	print('')
	print('--------------------------------------------------------------------------------')

def home_EZ():
	#set torque to full
	SendToEZ("/1m100<CR>\r")
	SendToEZ("/1l100<CR>\r")

	#Set fast speed and fast home - redundancy in case of 'jam'
	SendToEZ("/1v1500" + "Z10000R<CR>\r")
	SendToEZ("/1v1500" + "Z100R<CR>\r")
	SendToEZ("/1v1500" + "Z10000R<CR>\r")
	
	# do it very slow
	# ADL June 14
	SendToEZ("/1v200" + "Z10000R<CR>\r")
	SendToEZ("/1v200" + "Z100R<CR>\r")
	SendToEZ("/1v200" + "Z10000R<CR>\r")
	
#	xx = raw_input("wait to grease, hit enter")


	print('--------------------------------------------------------------------------------')
	print('')
	print('EZ: INTIALIZING/HOMING COMPLETE')
	print('')
	print('--------------------------------------------------------------------------------')
	EZ_GoTo_A(plungerLimit, 2000)
	return



#############################################################################
################### CONTROLLER COMMAND STRING GENERATORS ####################
##################### * SPEED AND INDEXING FUNCTIONS * ######################
#############################################################################

def VLMX_SetSpeed(motor, speed):
	#Receives list of motors to set to specified speed
	SendToVelmex('C, S' + motor + 'M' + str(speed) + ', R')

def VLMX_GoTo_Coordinated_A(motor1,	 index1, motor2,	index2):
	global verbose
	# two axes will be indexed silumtaneously (absolute)
	if (int(motor1) < int(motor2)):
		tempMotor = motor1
		tempIndex = index1
		motor1 = motor2
		index1 = index2
		motor2 = tempMotor
		index2 = tempIndex
	if verbose:
		print(' Sending MOTOR[' + str(motor1) + '] to INDEX[' + str(index1) + ']')
		print(' Sending MOTOR[' + str(motor2) + '] to INDEX[' + str(index2) + ']')
	SendToVelmex('C, (IA' + str(motor1) + 'M' + str(index1) + ', IA' + str(motor2) + 'M' + str(index2) + ',) R')

def VLMX_GoTo_A(motor, index): #ABSOLUTE
	global verbose
	#Receives list of commands of motors to set to specified distances 
	# index = '-0' indexes to zero motor position
	# index = 'x' indexes positive x index
	# index = '-x' indexes negative x index
	SendToVelmex('C, IA' + str(motor) + 'M' + str(index) + ', R')
	if verbose:
		print(' Sending MOTOR[' + str(motor) + '] to INDEX[' + str(index) + ']')

def VLMX_GoTo_R(motor, distance):
	#relative indexing
	#used only for tip ejection
	global verbose
	SendToVelmex('C, I' + str(motor) + 'M' + str(index) + ', R')
	if verbose:
		print(' Sending MOTOR[' + str(motor) + '] this many steps --> [' + str(distance) + ']')

def EZ_GoTo_A(index, speed): #Absolute with speed 
	global verbose
	#example: EZ.write('/1A10000R\r') moves to absolute position of 10000
	SendToEZ('/1V' + str(speed) + 'A' + str(index) + 'R<CR>\r')

def setVelmexToOnlineMode():
	velmex.flushInput()
	time.sleep(0.05)
	velmex.flushOutput()
	time.sleep(0.05)
	velmex.write('F') #Enable On-Line mode with echo "off"
	time.sleep(0.05)

def SendToVelmex(command):
	# an attempt to make sure there is not a caret in the serial buffer
	velmex.flushInput()
	time.sleep(0.05)
	velmex.flushOutput()
	time.sleep(0.05)
	velmex.write('C')
	time.sleep(0.05)
	velmex.write(command)
	data_raw = ''
	while(True):
		time.sleep(0.05)
		bytesToRead = velmex.inWaiting()
		data_raw += velmex.read()
		if '^' in data_raw:
			break
	#  extra check added
	velmex.flushInput()
	time.sleep(0.05)
	velmex.flushOutput()
	time.sleep(0.05)
	velmex.write('V')
	data_raw = ''
	while(True):
		time.sleep(0.05)
		bytesToRead = velmex.inWaiting()
		data_raw += velmex.read()
		if 'R' in data_raw:
			break
	print(command + '\t' + data_raw)

def SendToEZ(command):
#	global verbose
#	if verbose:
#		print('			EZ CMD: ' + command)
	# get the temperature of the Raspberry PI board and print it out
	# temp = subprocess.Popen(["vcgencmd","measure_temp"],stdout=subprocess.PIPE)
	# print (temp.communicate())
	EZ.write(command)
	time.sleep(0.3)
	while True:
		try:
			temp = EZ.readline()
		except serial.serialutil.SerialException:
			# print(temp)
			print("Serial Exception Detected")
			return ""
		else:
			if '`' not in temp:
				EZ.write("/1QR<CR>\r")
				time.sleep(0.3)
			else:
				break

#############################################################################
##################### ROBOT ACTUATION/ACTION FUNCTIONS ######################
#############################################################################


def aspirate(vol, depth = 100, speed = 100, test="False", mix=0):
	global verbose
	#INPUT VOLUME IN MICROLITERS
	# depth and speed are specified in percentages (max 100) INT! speeds and depths default to 100
	global currentDisplacement

	userPause()
	vol = float(vol)
	if(vol > maxUL):
		print("max volumn exceeded\n")
		exit()

	if verbose:
		print('Aspirating: ' + str(vol) + 'ul' + ' at ' + str(depth) + 'percent depth and ' + str(speed) + 'percent speed.')
	else:
		print('Aspirating')

	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	maxDepth = matrix[currentx][currenty].maxDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	targetDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * depth/100))
	targetSpeed = int(ezFast * speed/100)
	volume = int(vol * stepsPerUL)
	airgap = int(10 * stepsPerUL)
	#Lower ZMotor so tip is at right height
	EZ_GoTo_A(plungerLimit - airBuffer, ezFast)

	if test=="True":
		VLMX_GoTo_A(ZMotor, surfaceDepth)
		VLMX_SetSpeed(ZMotor, 2*ZSpeedSlow)
		VLMX_GoTo_A(ZMotor, targetDepth)
		VLMX_SetSpeed(ZMotor, ZSpeedFast)
	else:
		VLMX_GoTo_A(ZMotor, targetDepth)	

	# mix
	for i in range(mix):
		EZ_GoTo_A(plungerLimit - volume, targetSpeed)
		EZ_GoTo_A(plungerLimit, targetSpeed)
	# suck
	EZ_GoTo_A(plungerLimit - airBuffer - volume, targetSpeed)
	
	time.sleep(0.5)
	#move head to safe depth
	VLMX_GoTo_A(ZMotor, safeDepth)
	EZ_GoTo_A(plungerLimit - airBuffer - volume - airgap, targetSpeed)
	#for safety draw some more air
	#Update global variable for current syringe position
	currentDisplacement = plungerLimit - airBuffer - volume - airgap

def dispense(vol, depth = 100, speed = 100, test="False"):
	global verbose
	#INPUT VOLUME IN MICROLITERS
	# depth and speed are specified in percentages (max 100) INT! speeds and depths default to 100
	global currentDisplacement

	userPause()
	vol = float(vol)
	if(vol > maxUL):
		print("max volumn exceeded\n")
		exit()

	if verbose:
		print('			 Dispensing: ' + str(vol) + 'ul' + ' at ' + str(depth) + 'percent depth and ' + str(speed) + 'percent speed.')
	else:
		print('			 Dispensing')
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	maxDepth = matrix[currentx][currenty].maxDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	targetDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * depth/100))
	targetSpeed = int(ezFast * speed/100)
	volume = int(vol * stepsPerUL)
	airgap = int(10 * stepsPerUL)
	#Lower ZMotor so tip is at right height
	if test=="True":
		VLMX_GoTo_A(ZMotor, surfaceDepth)
		VLMX_SetSpeed(ZMotor, 2*ZSpeedSlow)
		VLMX_GoTo_A(ZMotor, targetDepth)
		VLMX_SetSpeed(ZMotor, ZSpeedFast)
	else:
		VLMX_GoTo_A(ZMotor, targetDepth)
	EZ_GoTo_A(currentDisplacement + volume + airBuffer + airgap, targetSpeed)
	currentDisplacement = currentDisplacement + volume + airBuffer + airgap
	#slow ascent
	time.sleep(0.5)
	VLMX_GoTo_A(ZMotor, safeDepth)
	#Update global variable for current syringe position

def moveAspirate(vol, startdepth = 20, enddepth = 80, speed = 50):
	global verbose
	#INPUT VOLUME IN MICROLITERS
	# depth and speed are specified in percentages (max 100) INT! speeds and depths default to 100
	# 0 is top and 100 bottom
	global currentDisplacement

	userPause()
	vol = float(vol)
	if(vol > maxUL):
		print("max volumn exceeded\n")
		exit()

	if verbose:
		print('Aspirating: ' + str(vol) + 'ul' + ' at ' + str(startdepth) + 'percent depth and ' + str(speed) + 'percent speed.')
	else:
		print('Aspirating')

	nsteps = 10
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	maxDepth = matrix[currentx][currenty].maxDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	targetstartDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * startdepth/100))
	targetendDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * enddepth/100))
	targetSpeed = int(ezFast * speed/100)
	volume = vol * stepsPerUL / nsteps
	airgap = int(10 * stepsPerUL)
	stepsize = (targetendDepth - targetstartDepth)/nsteps
	#Lower ZMotor so tip is at right height
	EZ_GoTo_A(plungerLimit - airBuffer, ezFast)

#	VLMX_GoTo_A(ZMotor, surfaceDepth)
#	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	for i in list(range(nsteps)):
		VLMX_GoTo_A(ZMotor, int(targetstartDepth + i*stepsize))
		#suck
		EZ_GoTo_A(plungerLimit - airBuffer - int((i+1) * volume), targetSpeed) 
	time.sleep(0.1)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, safeDepth)
	EZ_GoTo_A(plungerLimit - airBuffer - int((i+1) * volume) - airgap, targetSpeed)
	currentDisplacement = plungerLimit - airBuffer - int(nsteps * volume) - airgap

def moveDispense(vol, startdepth = 80, enddepth=20, speed = 50):
	global verbose
	#INPUT VOLUME IN MICROLITERS
	# depth and speed are specified in percentages (max 100) INT! speeds and depths default to 100
	global currentDisplacement

	userPause()
	vol = float(vol)
	if(vol > maxUL):
		print("max volumn exceeded\n")
		exit()
		
	if verbose:
		print('			 Dispensing: ' + str(vol) + 'ul' + ' at ' + str(startdepth) + 'percent depth and ' + str(speed) + 'percent speed.')
	else:
		print('			 Dispensing')
	nsteps = 10
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	maxDepth = matrix[currentx][currenty].maxDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	targetstartDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * startdepth/100))
	targetendDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * enddepth/100))
	targetSpeed = int(ezFast * speed/100)
	volume = vol * stepsPerUL / nsteps
	airgap = int(10 * stepsPerUL)
	stepsize = (targetendDepth - targetstartDepth)/nsteps
	
#	VLMX_GoTo_A(ZMotor, surfaceDepth)
#	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	for i in list(range(nsteps)):
		VLMX_GoTo_A(ZMotor, int(targetstartDepth + i*stepsize))
		#blow
		EZ_GoTo_A(currentDisplacement + int((i+1) * volume) + airgap, targetSpeed) 
	EZ_GoTo_A(currentDisplacement + int((i+1) * volume) + airBuffer + airgap, targetSpeed) 	
	time.sleep(0.1)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, safeDepth)
	currentDisplacement = currentDisplacement + airBuffer + int(nsteps*volume) + airgap

def mix(vol,depth,speed,mixcycles):
	
	global currentDisplacement
	vol = float(vol)
	if(vol > maxUL):
		print("max volumn exceeded\n")
		exit()
	
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	maxDepth = matrix[currentx][currenty].maxDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	targetDepth = int(surfaceDepth + ((maxDepth - surfaceDepth) * depth/100))
	targetSpeed = int(ezFast * speed/100)
	volume = int(vol * stepsPerUL)
	#Lower ZMotor so tip is at right height
	EZ_GoTo_A(plungerLimit - airBuffer, ezFast)
	VLMX_GoTo_A(ZMotor, targetDepth)	

	# mix
	for i in range(mixcycles):
		EZ_GoTo_A(plungerLimit - volume - airBuffer, targetSpeed)
		EZ_GoTo_A(plungerLimit - airBuffer, targetSpeed)
		time.sleep(0.5)

	time.sleep(0.5)
	#move head to safe depth
	VLMX_GoTo_A(ZMotor, safeDepth)
	#Update global variable for current syringe position
	currentDisplacement = plungerLimit - airBuffer

def liquidDisposal():
	userPause()
	print('Disposing Liquid')
	position(3, 1)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].surfaceDepth)
	EZ_GoTo_A(plungerLimit, ezSlow)
	EZ_GoTo_A(plungerLimit, ezSlow)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)

def disposeTips():
	userPause()
	print('Disposing Tips')
#	distance = 780
	distance = 840   
	# #mm to move * 39.5 steps/mm
	# height of hook entrance = hookEntrance
	# height of tip dispense = tipDispenseDepth
	position(2, 0)
	position_internal(3, 0)	
		
	VLMX_SetSpeed(XMotor, XSpeedFast)
	VLMX_SetSpeed(YMotor, YSpeedFast)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
#	VLMX_SetSpeed(XMotor, XSpeedSlow)
#	VLMX_SetSpeed(YMotor, YSpeedSlow)
#	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].maxDepth)		
	currentYIndex = matrix[currentx][currenty].y
	VLMX_GoTo_A(YMotor, currentYIndex + distance)	
#	VLMX_SetSpeed(XMotor, XSpeedSlow)
#	VLMX_SetSpeed(YMotor, YSpeedSlow)
#	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].ejectDepth)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].maxDepth)
	VLMX_GoTo_A(YMotor, currentYIndex)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)
#	EZ_GoTo_A(plungerLimit, ezSlow)
	VLMX_SetSpeed(XMotor, XSpeedFast)
	VLMX_SetSpeed(YMotor, YSpeedFast)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	
	position(2,0)

########################### MISC. SUPPORT FUNCTIONS #########################

def oldposition(row, col, position = 'UL'):
	userPause()
	global verbose
	global currentx
	global currenty
	destrow = row
	destcol = col
	currrow = currentx
	currcol = currenty
	if destrow == 3 and currcol == 0:
		position_internal(currrow, 1)
	if currrow == 3 and destcol == 0:
		position_internal(2, currcol)
	position_internal(destrow, destcol, position)

def position(row, col, position = 'UL'):
	userPause()
	global verbose
	global currentx
	global currenty
	destrow = row
	destcol = col
	currrow = currentx
	currcol = currenty
	if not (currrow == destrow and currcol == destcol):
		if currrow == 3:
			position_internal(2, currcol)
		if destrow == 3:
			position_internal(2, destcol)
	position_internal(destrow, destcol, position)

def position2(row, col, position = 'UL'):
	userPause()
	global verbose
	global currentx
	global currenty
	destrow = row
	destcol = col
	currrow = currentx
	currcol = currenty
	if not (currrow == destrow and currcol == destcol):
		if currrow == 3 and destcol == 0:
			position_internal(2, currcol)
		if destrow == 3 and currcol == 0:
			position_internal(currrow, 1)
	position_internal(destrow, destcol, position)

def position_internal(row, col, position = 'UL'):
	global verbose
	global currentx
	global currenty
	updateCurrentPos(row,col)
	try:
		if (position == None or matrix[row][col].sequence == None):
			pass
		else:
			try:
				matrix[row][col].reconfig(position)
			except Exception as e:
				print('Error - perhaps readdress is not permitted for this plate')
				print(e)
				traceback.print_exc(file=sys.stdout)
				terminate()
		#go to plate position
		VLMX_GoTo_Coordinated_A(YMotor, matrix[row][col].y, XMotor, matrix[row][col].x)
	
	except Exception as e:
		print(e)
		print('			 ****WARNING[position()]: INVALID PIPETTING COMMAND - consider revising .pipet file!')
		enterToContinue()
		
		print('			 ****Confirm no cross-contamination risk.')
		enterToContinue()
		
		print('			 ****Confirm that current plate address can be safely bypassed.')
		enterToContinue()

def updateCurrentPos(row, col):
	global currentx
	global currenty
	currentx = row
	currenty = col

def enterToContinue():
	print('-> Press Enter to Continue')
	try:
		input= raw_input()
	except NameError:
		pass
	
############################# SHUT DOWN FUNCTIONS ###########################
def ShutDownRobot(DOvelmex=True,DOEZ=True):
	print('Initiating shutdown - Returning to home position. Please Wait')
	if(DOvelmex):
		print('Homing to safety')
		home_Velmex()
		velmex.close()
	if(DOEZ):
		home_EZ()
		EZ.close()
	print('Good Bye!')
	sys.exit(0)

############################# ADL re-writes #################################
	
def loadTips():
	userPause()
	global verbose
	global currentx
	global currenty
	guess = raw_input("Do you need to load tips (y/n)?")
	if guess == "y":
		VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)
		position(0,6)
		print('***Press Enter to Continue ****')
		enterToContinue()

def retrieveTips(CurrentTipPosition, align="False"):
	userPause()
	global verbose
	global currentx
	global currenty
	global currentDisplacement
#	CurrentTipPosition = 2    # debug
# get more tips if empty
	if (CurrentTipPosition >24):
		CurrentTipPosition = 1
		position(0,6)
		print('NO MORE AVAILABLE TIPS!')
		print('*******The head has been moved out of the way.*******')
		print('***Please reload tip box holders before continuing.***')
		print('***Press Enter to Continue ****')
		enterToContinue()
	BoxDict = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F'}
	OffsetDict = {1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
	BoxLocation = {'A':[0,0],'B':[0,1],'C':[1,0],'D':[1,1],'E':[2,0],'F':[2,1]}
	tiplookuptable = 	{1:[1,1],2:[1,2],3:[1,3],4:[1,4], 5:[2,1],6:[2,2],7:[2,3],8:[2,4], 9:[3,1],10:[3,2],11:[3,3],12:[3,4], 13:[4,1],14:[4,2],15:[4,3],16:[4,4], 17:[5,1],18:[5,2],19:[5,3],20:[5,4], 21:[6,1],22:[6,2],23:[6,3],24:[6,4]}
	Box = BoxDict[tiplookuptable[CurrentTipPosition][0]]
	offset = OffsetDict[tiplookuptable[CurrentTipPosition][1]]
	row = BoxLocation[Box][0]
	col = BoxLocation[Box][1]
	print('Retrieving Tips')
	position(row, col, offset)
	EZ_GoTo_A(plungerLimit, ezFast) 
	currentDisplacement = plungerLimit
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].surfaceDepth) #depth to go before slowing down

	if align=="True":
		VLMX_SetSpeed(ZMotor, ZSpeedSlow)
		VLMX_SetSpeed(XMotor, XSpeedSlow)
		VLMX_SetSpeed(YMotor, YSpeedSlow)
		answer="Y"
		XGuess = 0.0
		YGuess = 0.0
		ZGuess = 0.0
		while answer == "Y":
			print("Now the X offset")
			guess = 10.0
			while guess != 0.0:
				guess = 40.0*float(raw_input("number of mm RIGHT (+tv) or LEFT (-tv) or 0 exits ?"))
				XGuess = XGuess + guess
				VLMX_GoTo_Coordinated_A(YMotor, matrix[row][col].y, XMotor, matrix[row][col].x + XGuess)

			print("Next the Y offset")
			guess = 10.0
			while guess != 0.0:
				guess = 40.0*float(raw_input("number of mm FORWARD (+tv) or BACKWARD (-tv) or 0 exits ?"))
				YGuess = YGuess + guess
				VLMX_GoTo_Coordinated_A(YMotor, matrix[row][col].y + YGuess, XMotor, matrix[row][col].x + XGuess)
		
			VLMX_SetSpeed(ZMotor, ZSpeedSlow)
			print("Next the Z offset")
			guess = 10.0
			while guess != 0.0:
				guess = 160.0*float(raw_input("number of mm DOWN (+tv) or UP (-tv) or 0 exits ?"))
				ZGuess = ZGuess + guess
				VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].surfaceDepth + ZGuess)
			print ("Zoffset = ",ZGuess)
			
			answer = raw_input("Would you like to fine tune X,Y,Z (Y or N)?")
			
		#  these positions are relative to old settings
		print ("X offset = ",XGuess)
		print ("Y offset = ",YGuess)
		print ("Z offset = ",ZGuess)
		print ("Z position = ",matrix[currentx][currenty].surfaceDepth + ZGuess)


		VLMX_SetSpeed(ZMotor, ZSpeedFast)
		VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)
		VLMX_SetSpeed(XMotor, XSpeedFast)
		VLMX_SetSpeed(YMotor, YSpeedFast)
		VLMX_GoTo_A(ZMotor,s.universalSafeHeight)
	
	else:
		VLMX_SetSpeed(ZMotor, 4*ZSpeedSlow)
		VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].tipAttachDepth)
		VLMX_SetSpeed(ZMotor, ZSpeedFast)
		VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)
	
	CurrentTipPosition = CurrentTipPosition + 1
	return CurrentTipPosition
		
def newplate(row=0,col=2):
	# DO THIS AT POSITION --->>> 0,2
	#
	# if these positions are "off" for other plates, the problem is 
	#   the "PlateColumns" and "PlateRows" in "Classes"
	#	
	# define surfaceDepth
	# define X offset
	# define Y offset
	# define max depth
	#
	# use this to define the "UL" for 96 well plate
	# "UL" for 24 well plates is their center
	
	#  this routine is for define the center of a new plate sitting at position 0,2
	#  all the other plates should then be OK ... provides the corners of the plates are correctly defined.
	

	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	VLMX_SetSpeed(XMotor, XSpeedSlow)
	VLMX_SetSpeed(YMotor, YSpeedSlow)
	currentZ = s.universalSafeHeight
	currentX = C.XPositions[row][col]
	currentY = C.YPositions[row][col]
	VLMX_GoTo_A(ZMotor,currentZ)
	position(row,col)
	
	print("Lets get the Surface Height first, this is the height of the top of the plate")
	guess = 10.0
	while guess != 0.0:
		guess = 160.0*float(raw_input("number of mm DOWN (+tv) or UP (-tv) or 0 exits ?"))
		currentZ = currentZ + guess
		VLMX_GoTo_A(ZMotor,currentZ)
	print ("SurfaceHeight = ",currentZ)

	print("Now the X offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm RIGHT (+tv) or LEFT (-tv) or 0 exits ?"))
		currentX = currentX + guess
		VLMX_GoTo_A(XMotor,currentX)
	print ("X offset = ",currentX-C.XPositions[row][col])

	print("Next the Y offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm FORWARD (+tv) or BACKWARD (-tv) or 0 exits ?"))
		currentY = currentY + guess
		VLMX_GoTo_A(YMotor,currentY)
	print ("Yoffset = ",currentY-C.YPositions[row][col])

	print("finally the max depth")
	guess = 10.0
	while guess != 0.0:
		guess = 160.0*float(raw_input("number of mm DOWN (+tv) or UP (-tv) or 0 exits ?"))
		currentZ = currentZ + guess
		VLMX_GoTo_A(ZMotor,currentZ)
	print ("Maxdepth = ",currentZ)
	
	print("Finetune the X offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm RIGHT (+tv) or LEFT (-tv) or 0 exits ?"))
		currentX = currentX + guess
		VLMX_GoTo_A(XMotor,currentX)
	print ("X offset = ",currentX-C.XPositions[row][col])

	print("Finetune the Y offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm FORWARD (+tv) or BACKWARD (-tv) or 0 exits ?"))
		currentY = currentY + guess
		VLMX_GoTo_A(YMotor,currentY)
	print ("Yoffset = ",currentY-C.YPositions[row][col])
	
	VLMX_GoTo_A(ZMotor,s.universalSafeHeight)
	return
	

###  not sure what this routine does.  
def testplate():
	global currentDisplacement
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	safeDepth = matrix[currentx][currenty].safeDepth
	#Lower ZMotor so tip is at right height
	VLMX_GoTo_A(ZMotor, surfaceDepth)
	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	VLMX_SetSpeed(XMotor, XSpeedSlow)
	VLMX_SetSpeed(YMotor, YSpeedSlow)

	print("Now the X offset")
	guess = 10.0
	Guess = 0.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm RIGHT (+tv) or LEFT (-tv) or 0 exits ?"))
		Guess = Guess + guess
		VLMX_GoTo_A(XMotor,currentx+Guess)
	print ("X offset = ",Guess)

	print("Next the Y offset")
	guess = 10.0
	Guess = 0.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm FORWARD (+tv) or BACKWARD (-tv) or 0 exits ?"))
		Guess = Guess + guess
		VLMX_GoTo_A(YMotor,currenty+Guess)
	print ("Yoffset = ",Guess)

	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_SetSpeed(XMotor, XSpeedFast)
	VLMX_SetSpeed(YMotor, YSpeedFast)
	#move head to safe depth
	VLMX_GoTo_A(ZMotor, safeDepth)
           			
def defineCornersOf24WellPlates(row=0,col=2):
	# Cycle through all position and define the upper left corner of each plate
	# DO this with a "BLANK" plate definition at each position
	

	VLMX_SetSpeed(ZMotor, ZSpeedSlow)
	VLMX_SetSpeed(XMotor, 5*XSpeedSlow)
	VLMX_SetSpeed(YMotor, 5*YSpeedSlow)
	currentX = C.XPositions[row][col]
	currentY = C.YPositions[row][col]
	VLMX_GoTo_A(ZMotor,s.universalSafeHeight)
	position(row,col)
	surfaceDepth = matrix[currentx][currenty].surfaceDepth
	currentZ = surfaceDepth
	VLMX_GoTo_A(ZMotor,surfaceDepth)
	
	print("Lets get the Surface Height first, this is the height of the top of the plate")
	guess = 10.0
	while guess != 0.0:
		guess = 160.0*float(raw_input("number of mm DOWN (+tv) or UP (-tv) or 0 exits ?"))
		currentZ = currentZ + guess
		VLMX_GoTo_A(ZMotor,currentZ)
	print ("HeightCorrection = ",currentZ-surfaceDepth)

	print("Now the X offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm RIGHT (+tv) or LEFT (-tv) or 0 exits ?"))
		currentX = currentX + guess
		VLMX_GoTo_A(XMotor,currentX)
	print ("X offset = ",currentX-C.XPositions[row][col])

	print("Next the Y offset")
	guess = 10.0
	while guess != 0.0:
		guess = 40.0*float(raw_input("number of mm FORWARD (+tv) or BACKWARD (-tv) or 0 exits ?"))
		currentY = currentY + guess
		VLMX_GoTo_A(YMotor,currentY)
	print ("Yoffset = ",currentY-C.YPositions[row][col])
	
	VLMX_GoTo_A(ZMotor,s.universalSafeHeight)
	return
	
def userPause():
# if the user hits the return key during program execution
# the program will pause at the start of the next step
  i,o,e = select.select([sys.stdin],[],[],0.0001)
  for s in i:
    if s == sys.stdin:
      input = sys.stdin.readline()
      print('The program has detected a USER pause')
      myraw = raw_input('press <ENTER> to continue')

def extraSeatTips():
	userPause()
	global verbose
	global currentx
	global currenty
	global currentDisplacement
	#  position "F" 1st offset
	InternalTipPosition = 21
	# thickness of glued on thing in mm * 159 = 5.6 mm * 159 = 890
	extraHeightOffset = 890
	BoxDict = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F'}
	OffsetDict = {1: 'UL', 2: 'UR', 3: 'LL', 4: 'LR'}
	BoxLocation = {'A':[0,0],'B':[0,1],'C':[1,0],'D':[1,1],'E':[2,0],'F':[2,1]}
	tiplookuptable = 	{1:[1,1],2:[1,2],3:[1,3],4:[1,4], 5:[2,1],6:[2,2],7:[2,3],8:[2,4], 9:[3,1],10:[3,2],11:[3,3],12:[3,4], 13:[4,1],14:[4,2],15:[4,3],16:[4,4], 17:[5,1],18:[5,2],19:[5,3],20:[5,4], 21:[6,1],22:[6,2],23:[6,3],24:[6,4]}
	Box = BoxDict[tiplookuptable[InternalTipPosition][0]]
	offset = OffsetDict[tiplookuptable[InternalTipPosition][1]]
	row = BoxLocation[Box][0]
	col = BoxLocation[Box][1]
	print('Extra seating of tips at box F')
	position(row, col, offset)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].surfaceDepth - extraHeightOffset) #depth to go before slowing down
	VLMX_SetSpeed(ZMotor, 4*ZSpeedSlow)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].tipAttachDepth - extraHeightOffset)
	VLMX_SetSpeed(ZMotor, ZSpeedFast)
	VLMX_GoTo_A(ZMotor, matrix[currentx][currenty].safeDepth)		

