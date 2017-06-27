#Last Update Apr 13 2016 by Eric Huang: Add new plate objects, LP24P name changed to DW24P
#Last Update Feb 29 2016 by Eric Huang: Remove superfluous functions, simplifying control code per P.Long's preference
#Last Update Feb 19 2016 by Eric Huang
#Last Update Feb 18 2016 by Eric Huang
# June 16 == ADL edited plate definitions

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
   {'x':440,\
    'y':320,\
    'alignmentDepth': 2300,\
    'surfDepth': 2540,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 8460,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': wellDist,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'DW24P': \
   {'x':580,\
    'y':472,\
    'alignmentDepth': 2300,\
    'surfDepth': 2364,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 8124,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': None,\
    'readdress': None},\
'SW96P': \
   {'x':460,\
    'y':352,\
    'alignmentDepth': 2300,\
    'surfDepth': 3420, \
    'safeDepth':universalSafeHeight,\
    'maxDepth': 4940,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': wellDist,\
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'SW24P': \
   {'x':620,\
    'y':552,\
    'alignmentDepth': 2300,\
    'surfDepth': 2700,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 5200,\
    'tipAttachDepth': None, \
    'ejectDepth': None, \
    'wellDist': None,\
    'readdress': None},\
'RES41': \
   {'x':580,\
    'y':475,\
    'alignmentDepth': 2300,\
    'surfDepth': 2364,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 8120,\
    'tipAttachDepth': None,\
    'ejectDepth': None,\
    'wellDist': None, \
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
    'readdress': None},\
'TBOXA': \
   {'x':56,\
    'y':944,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXB': \
   {'x':204,\
    'y':984, \
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXC': \
   {'x':-8,\
    'y':1206,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXD': \
   {'x':179,\
    'y':1222,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXE': \
   {'x':-30,\
    'y':1454,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TBOXF': \
   {'x':162,\
    'y':1472,\
    'alignmentDepth': STDalignmentDepth,\
    'surfDepth': 14200,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': None,\
    'tipAttachDepth': STDtipAttach,\
    'ejectDepth': None,\
    'wellDist': wellDist, \
    'readdress':{'UL':[0, 0],'UR': [1, 0], 'LL':[0, 1], 'LR':[1, 1]}},\
'TDISP': \
   {'x':8,\
    'y':2100,\
    'alignmentDepth': 2300,\
    'surfDepth': 3800,\
    'safeDepth':universalSafeHeight,\
    'maxDepth': 10140,\
    'tipAttachDepth': None, \
    'ejectDepth': 7500, \
    'wellDist': None,\
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
    'readdress': None}\
}

#plate positions
PlateColumns = [125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632]
PlateRows = [170, 3923, 7681, 11409]

####  *Positions index the X and Y positions as a function of all positive 40 offsets
XPositions = [[125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632],
								[125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632],
								[125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632],
								[125, 5683, 11650, 16916, 22202, 27488, 32774, 38060, 43346, 48632]]
YPositions = [[170, 170, 178, 170, 170, 190, 182, 186, 178, 178],
								[3923, 3923, 3927, 3927, 3974, 3951, 3947, 3935, 3943, 3931],
								[7681, 7681, 7685, 7681, 7681, 7701, 7697, 7705, 7681, 7693],
								[11409, 11409, 11433, 11449, 11437, 11445, 11445, 11449, 11445, 11441]]
								
ZPositions = [[0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0],
						[0,0,0,0,0,0,0,0,0,0]]

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
		self.maxDepth = plateInfo[self.plateType]['maxDepth'] + ZPositions[self.row][self.col]
		self.surfaceDepth = plateInfo[self.plateType]['surfDepth'] + ZPositions[self.row][self.col]
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
