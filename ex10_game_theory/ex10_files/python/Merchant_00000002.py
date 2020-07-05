import numpy as np

def Merchant_00000002(history):
	# Returns choice of 0 or 1
	# 0 - Low
	# 1 - High
	# history is aan array of 2xN previous choices:
	# the upper row is the previous choices of the player,
	# and the lower row is the previous choices of the other player.
	# Note that history may be empty!

	return np.random.randint(2)
	
