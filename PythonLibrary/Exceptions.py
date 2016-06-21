'''
This module is for defining class definitions of exceptions that should be raised
during program runtime. For example - program verification exceptions
'''


#######################################################################################
#######################################################################################
#######################################################################################
################################### CLASS DEFINITIONS #################################
#######################################################################################
#######################################################################################
#######################################################################################

class badVolumes(Exception):
	def __init__(self):
		print('')
		print('')
		print('')
		print('-------------------------------------------------------------------------------')
		#raise this exception if there are bad volume paramters in the .pipet file
		print('      -->ERROR! Selected program has failed command verification.')
		print('      This is due to:')
		print('      -->Volume input paramter(s) for one or more aspirate()/dispense()')
		print('         is out of bounds. Volume should be specified in microliter units,')
		print('         between 0 and 1000')
		print('')
		print('      *Shutdown for safety*')
		print('-------------------------------------------------------------------------------')
		print('')
		print('')
		terminate()

class badAssignment(Exception):
	def __init__(self):
		print('')
		print('')
		print('')
		print('-------------------------------------------------------------------------------')
		#raise this exception if there are bad volume paramters in the .pipet file
		print('      -->ERROR! One or more assignments made in .pipet file is invalid')
		print('      -->Revise and rerun program')
		print('')
		print('      *Shutdown for safety*')
		print('-------------------------------------------------------------------------------')
		print('')
		print('')
		terminate()

class badPosition(Exception):
	def __init__(self):
		print('')
		print('')
		print('')
		print('-------------------------------------------------------------------------------')
		#raise this exception if there are bad volume paramters in the .pipet file
		print('      -->ERROR! Function arguments for position(x, y) function is invalid')
		print('      -->Revise and rerun program')
		print('')
		print('      *Shutdown for safety*')
		print('-------------------------------------------------------------------------------')
		print('')
		print('')
		terminate()

class badTipBox(Exception):
	def __init__(self):
		print('')
		print('')
		print('')
		print('-------------------------------------------------------------------------------')
		#raise this exception if there are bad volume paramters in the .pipet file
		print('      -->ERROR! Function arguments for retrieveTips() function is invalid')
		print('      -->Revise and rerun program')
		print('')
		print('      *Shutdown for safety*')
		print('-------------------------------------------------------------------------------')
		print('')
		print('')
		terminate()