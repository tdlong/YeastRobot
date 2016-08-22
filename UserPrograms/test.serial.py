import serial #for communicating to controllers through serial ports

def VLMX_SetSpeed(motor, speed):
	#Receives list of motors to set to specified speed
	SendToVelmex('C, S' + motor + 'M' + str(speed) + ', R')

def VLMX_GoTo_Coordinated(motor1,	 index1, motor2,	index2):
	global verbose
	# two axes will be indexed silumtaneously (relative)
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
	SendToVelmex('C, (I' + str(motor1) + 'M' + str(index1) + ', I' + str(motor2) + 'M' + str(index2) + ',) R')

def VLMX_GoTo(motor, index): #RELATIVE
	global verbose
	#Receives list of commands of motors to set to specified distances
	# index = '-0' indexes to zero motor position
	# index = 'x' indexes positive x index
	# index = '-x' indexes negative x index
	SendToVelmex('C, I' + str(motor) + 'M' + str(index) + ', R')
	if verbose:
		print(' Sending MOTOR[' + str(motor) + '] to INDEX[' + str(index) + ']')

def SendToVelmex(command):
#	global verbose
#	if verbose:
#		print('VLMX CMD: ' + command)
#		velmex.write('C, V, R')
#		count = 0
#		while(True):
#			count += 1
#			returnstatus = velmex.read()
#			if ('R' in returnstatus or '^' in returnstatus or count >= 100):
#				break
	velmex.write('F') #Enable On-Line mode with echo "off"
	velmex.write(command)
	data_raw = ''
	while(True):
		time.sleep(0.1)
		bytesToRead = velmex.inWaiting()
		data_raw += velmex.read()
		if '^' in data_raw:
			break
	return



VLMXserialPort = '/dev/ttyUSB1'
EZserialPort = '/dev/ttyUSB0'
BR = 9600
XSpeedFast = 3500
YSpeedFast = 3500 
ZSpeedFast = 4500


global velmex
global VLMXserialPort

global EZ
global EZserialPort
	
velmex = serial.Serial(port= VLMXserialPort, baudrate = BR, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
velmex.open()
velmex.is_open
velmex.close()
velmex.is_open

VLMX_SetSpeed(ZMotor, int(0.5*ZSpeedFast))
VLMX_SetSpeed(XMotor, int(0.5*XSpeedFast))
VLMX_SetSpeed(YMotor, int(0.5*YSpeedFast))
absZero = '-0'
VLMX_GoTo(ZMotor, absZero)
VLMX_GoTo_Coordinated(XMotor, absZero, YMotor, absZero)



