import Settings as s


#steps per mm, updated in Settings.py
xrate = s.xrate
yrate = s.yrate
zrate = s.zrate
prate = s.prate


def x(mm):
	global xrate
	print('')
	print('         -------------------------------')
	print('')
	print('         X Axis - Conversion: ')
	print('                Millimeters = ' + str(mm))
	print('                      Steps = ' + str(xrate*mm))
	print('')
	print('         -------------------------------')
	print('')

def y(mm):
	global yrate
	print('')
	print('         -------------------------------')
	print('')
	print('         Y Axis - Conversion: ')
	print('                Millimeters = ' + str(mm))
	print('                      Steps = ' + str(yrate*mm))
	print('')
	print('         -------------------------------')
	print('')
		
def z(mm):
	global zrate
	print('')
	print('         -------------------------------')
	print('')
	print('         Z Axis - Conversion: ')
	print('                Millimeters = ' + str(mm))
	print('                      Steps = ' + str(zrate*mm))
	print('')
	print('         -------------------------------')
	print('')
	
def p(mm):
	global prate
	print('')
	print('         -------------------------------')
	print('')
	print('         P Axis - Conversion: ')
	print('                Millimeters = ' + str(mm))
	print('                      Steps = ' + str(prate*mm))
	print('')
	print('         -------------------------------')
	print('')
	

def main():
	print('--------------------------------------------------------------------------------')
	print('')
	print('                             MM TO STEPS CONVERSION')
	print('')
	print('--------------------------------------------------------------------------------')
	print('')
	print('')
	while(True):
		print('         Which axis are you calculating?')
		print('         -------------------------------')
		print('                1) X (Left and Right)')
		print('                2) Y (Closer and Farther)')
		print('                3) Z (Up and Down)')
		print('                4) P (Pipetting Axis)')
		print('         -------------------------------')
		try:
			select = int(input('               Selection:'))
			mm = float(input('             Millimeters:'))
		except:
			print('')
			print('         INVALID INPUT - TRY AGAIN')
			print('')
		if (int(select) in [1, 2, 3, 4]):
			if (mm > 0.0):
				break
		else:
			print('         INVALID INPUT - TRY AGAIN')

	if select == 1:
		x(mm)
	if select == 2:
		y(mm)
	if select == 3:
		z(mm)
	if select == 4:
		p(mm)

if __name__ == '__main__':
	main()