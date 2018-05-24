#Last Update Apr 13 2016 by Eric Huang: Add new plate objects, LP24P name changed to DW24P
#Last Update Feb 29 2016 by Eric Huang: Remove superfluous functions, simplifying control code per P.Long's preference
#Last Update Feb 19 2016 by Eric Huang
#Last Update Feb 18 2016 by Eric Huang
# June 16 == ADL edited plate definitions

#XYZ step conversion
# xrate = 39.5 #steps per mm for X AXIS
# yrate = 39.5 #steps per mm for Y AXIS
# zrate = 159 #steps per mm for Z AXIS


import Settings as s

'''
plateInfo Dictionary Guide - dict(dict())
	'x': (int)
		x step offset to get to top left well
		*REQUIRED FOR ALL PLATES
	'y': (int)
		y step offset to get to top left well 
		*REQUIRED FOR ALL PLATES
        'surfDepth': (int)
                depth of the very top surface of the well. tips are not yet inside well.
	'safeDepth': (int)
		maximum depth that pipet tip should retreat to for safe XY travel(a little higher than surfDepth)
	'maxDepth': (int)
		maximum depth that pipet tip is allowed to plunge
		*REQUIRED FOR ALL PLATES
        'tipAttachDepth': (int)
                depth at which syringes are lowered and pressed into tips to retrieve them
        'ejectDepth': (int)
                depth at which ejection should occur
        'wellDist': (int)
		number of steps between each well on the plate (assuming x and y are the same unit distances)
	'readdress': (dict(list()))
		dict of lists of unit directional data for readdressing procedure
			i.e. {UL:[0,1], LR:[1,-2]}
'''
STDalignmentDepth = s.STDalignmentDepth
STDtipAttach = s.STDtipAttach
universalSafeHeight = s.universalSafeHeight; #update to optimize speed, minimizing travel distance
wellDist = 350

plateInfo = {\
'DW96P': \
   {'x':468,\
    'y':328,\
    'alignmentDepth': 2300,\
    'surfDepth': 2460,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 8940,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': wellDist,\
    'deepWellOffset':True,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'DW96W': \
   {'x':476,\
    'y':344,\
    'alignmentDepth': 2300,\
    'surfDepth': 2460,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 9180,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': wellDist,\
    'deepWellOffset':True,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'DW24P': \
   {'x':640,\
    'y':520,\
    'alignmentDepth': 2300,\
    'surfDepth': 2540,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 8900,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': None,\
    'deepWellOffset':True,\
    'readdress': None},\
'SW96P': \
   {'x':520,\
    'y':300,\
    'alignmentDepth': 2300,\
    'surfDepth': 3600, \
    'safeDepth':universalSafeHeight,\
    'maxDepth': 5452,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': wellDist,\
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'SW24P': \
   {'x':640,\
    'y':540,\
    'alignmentDepth': 2300,\
    'surfDepth': 2860,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 5610,\
    'tipAttachDepth': None, \
    'ejectDepth': None, \
    'wellDist': None,\
    'deepWellOffset':False,\
    'readdress': None},\
'RES41': \
   {'x':480,\
    'y':480,\
    'alignmentDepth': 2300,\
    'surfDepth': 2860,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 9148,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': None, \
    'deepWellOffset':True,\
    'readdress': None},\
'RES6C': \
   {'x':640,\
    'y':540,\
    'alignmentDepth': 2300,\
    'surfDepth': 2860,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 9148,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': None, \
    'deepWellOffset':True,\
    'readdress': None},\
'BLANK': \
   {'x':0, \
    'y':0,\
    'alignmentDepth': 2300,\
    'surfDepth': 2900,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 0,\
    'tipAttachDepth': None,\
    'ejectDepth': None, \
    'wellDist': None, \
    'deepWellOffset':False,\
    'readdress': None},\
'TBOXA': \
   {'x':58,\
    'y':976,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 17125,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
   'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXB': \
   {'x':252,\
    'y':1000, \
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 17120,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXC': \
   {'x':20,\
    'y':1218,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 17020,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXD': \
   {'x':213,\
    'y':1228,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 17100,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXE': \
   {'x':22,\
    'y':1472,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 16980,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXF': \
   {'x':186,\
    'y':1466,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': 16980,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'deepWellOffset':False,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TDISP': \
   {'x':75,\
    'y':2100,\
    'alignmentDepth': 2300,\
    'surfDepth': 3800,\
    'safeDepth':universalSafeHeight,\
 #   'maxDepth': 10140,\
    'maxDepth': 10000,\
   'tipAttachDepth': None, \
    'ejectDepth': 7630, \
    'wellDist': None,\
    'deepWellOffset':False,\
   'readdress': None},\
        
'LWSTE': \
   {'x':-100,\
    'y':3300, \
    'alignmentDepth': 2300,\
    'surfDepth': 3800,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 5000, \
    'tipAttachDepth': None, \
    'ejectDepth': None, \
    'wellDist': None, \
    'deepWellOffset':False,\
    'readdress': None}\
}

#plate positions
PlateColumns = [125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632]
PlateRows = [170, 3923, 7681, 11409]

####  *Positions index the X and Y positions as a function of all positive 40 offsets
XPositions =                   [[125, 5683, 11610, 16900, 22182, 27428, 32724, 38000, 43300, 48580],
								[125, 5683, 11610, 16900, 22182, 27428, 32724, 38000, 43270, 48560],
								[125, 5683, 11610, 16900, 22182, 27428, 32724, 38000, 43230, 48540],
								[125, 5683, 11610, 16900, 22182, 27428, 32724, 38000, 43230, 48530]]
YPositions =                   [[170, 170, 203, 195, 195, 215, 215, 219, 203, 203],
								[3923, 3923, 3952, 3952, 3983, 3976, 3980, 3960, 3964, 3956],
								[7681, 7681, 7710, 7706, 7718, 7726, 7722, 7730, 7710, 7700],
								[11409, 11409, 11458, 11474, 11462, 11470, 11470, 11474, 11482, 11474]]
								
ZPositions = [[0,0,64,208,112,-80,0,64,64,0],
						[0,0,32,0,-48,-112,0,0,-64,-32],
						[0,0,-112,0,-192,-192,0,0,-144,-96],
						[0,0,-272,-160,-256,-240,-64,-112,-192,-160]]
						
lowZPositions = [[0,0,0,-160,0,128,0,0,0,80],
								[0,0,-80,0,0,0,0,0,32,0],
								[0,0,-80,-40,0,0,-80,-80,0,-80],
								[0,0,-208,-208,0,0,-80,-80,0,0]]

class Cell:
	#all the positioning data and manipulation for each cell
	def __init__(self, plate_type, addressROW, addressCOL):
		#cell identity
		self.plateType = plate_type #ie 'DW96P'
		self.row = addressROW
		self.col = addressCOL

		#dynamic coordinates (in the case of readdressing)
#		self.x = PlateColumns[self.col] + plateInfo[self.plateType]['x']
#		self.y = PlateRows[self.row] + plateInfo[self.plateType]['y']
		self.x = XPositions[self.row][self.col] + plateInfo[self.plateType]['x']
		self.y = YPositions[self.row][self.col] + plateInfo[self.plateType]['y']

		#static coordinates for permanent reference
		self.xP = self.x
		self.yP = self.y

		#precision position data
		self.wellSpacing = plateInfo[self.plateType]['wellDist']
		self.alignmentDepth = plateInfo[self.plateType]['alignmentDepth']
		self.safeDepth = plateInfo[self.plateType]['safeDepth']

#####  These can include a height correction for each position, to account for variation in the deck
#		self.maxDepth = plateInfo[self.plateType]['maxDepth']
#		self.surfaceDepth = plateInfo[self.plateType]['surfDepth']
		if plateInfo[self.plateType]['maxDepth'] is not None:
			self.maxDepth = plateInfo[self.plateType]['maxDepth'] + ZPositions[self.row][self.col]
			if plateInfo[self.plateType]['deepWellOffset']:
				self.maxDepth = self.maxDepth + lowZPositions[self.row][self.col]
		else:
			self.maxDepth = None
		if plateInfo[self.plateType]['surfDepth'] is not None:
			self.surfaceDepth = plateInfo[self.plateType]['surfDepth'] + ZPositions[self.row][self.col]
			if plateInfo[self.plateType]['deepWellOffset']:
				self.surfaceDepth = self.surfaceDepth + lowZPositions[self.row][self.col]
		else:
			self.surfaceDepth = None
####

		self.ejectDepth = plateInfo[self.plateType]['ejectDepth']
		self.tipAttachDepth = plateInfo[self.plateType]['tipAttachDepth']
        #readress sequence
		self.sequence = plateInfo[self.plateType]['readdress']

	def reset(self, position): #set back to initial position (before readdressing modifications)
		self.y = self.yP + (self.wellSpacing * self.sequence[position][1])
		self.x = self.xP + (self.wellSpacing * self.sequence[position][0])
	def reconfig(self, position):#CALL THIS if readdressing is needed
		self.x = self.xP + (self.wellSpacing * self.sequence[position][0])
		self.y = self.yP + (self.wellSpacing * self.sequence[position][1])
