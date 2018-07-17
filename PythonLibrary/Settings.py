'''
This py module stores variables that need to be accessed by the PipetControlFX module.
'''

import os

#####################General####################
version = '1.0.8'


#####################Serial IO####################
# VLMXserialPort = '/dev/ttyUSB-velmex'
# EZserialPort = '/dev/ttyUSB-ez'
VLMXserialPort = '/dev/ttyUSB0'
EZserialPort = '/dev/ttyUSB1'
BR = 9600

##################Speed Settings##################
#string assignemnt for MOTOR SPEED value
XSpeedFast = 3500 #fast speeds for velmex
YSpeedFast = 3500 
ZSpeedFast = 4000
XSpeedSlowP = 1000 #slow speeds for velemx for position when specified
YSpeedSlowP = 1000
ZSpeedSlowP = 3000
XSpeedSlow = 300 #slow speeds for velmex
YSpeedSlow = 300
ZSpeedSlow = 300
ZSpeedPipet = 300 #slow speeds for velmex pipetting action on z motor
ezSlow = 500 #slow speed for EZ stepper
ezFast = 2000 #fast speed for EZ stepper

#XYZ step conversion
xrate = 39.5 #steps per mm for X AXIS
yrate = 39.5 #steps per mm for Y AXIS
zrate = 159 #steps per mm for Z AXIS

################Head Index Settings###############
STDalignmentDepth = 1000 #standard depth for traversing close to plates for alignment
STDtipAttach = 17275      #standard depth to seat tips (dont go too low)
universalSafeHeight = 300 #height at which it is safe for the head to traverse in X/Y. This variable can be optimized for minimizing travel


###########Steps to Distance Conversion###########
#pipetting step conversion
#  ADL June 14, I calculate closer to 1.96 steps/ul
#  motor is 0.0079 steps/mm = 126.5823 steps/mm
#  syringe is 31mm = 2000ul -> 0.0155 mm/ul
#  the product is 1.96 is the controller 1/2 stepping ... actually the default is the 2 step
#  so this means that perhaps the 4 steps per ul is accurate
#  manual says /1j8R  would gives you 8X resolution etc.
stepsPerUL = 13.6 #steps per microliliter for P AXIS
prate = 200 #steps per mm for P AXIS

# if you changed the resolution of the stepper ... these would change
#Air buffer (extra air that is aspirated for safety and sample retention) in theory 2.5 ul
airBuffer = 10

#depth limit - when the plunger is at the very bottom of the syringe
plungerLimit = 5100
maxUL = plungerLimit/stepsPerUL - 5

#########Stuff you shouldnt have to touch#########

#Determine number of rows, cols
deck_rows = 4
deck_cols = 10

#File Reading
targetDir = os.getcwd() + '/Programs/' #Directory of .pipet program files









