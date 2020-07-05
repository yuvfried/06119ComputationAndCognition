import numpy as np

def Merchant_00000003(history):
	# Returns choice of 0 or 1
	# 0 - Low
	# 1 - High
	# history is aan array of 2xN previous choices:
	# the upper row is the previous choices of the player,
	# and the lower row is the previous choices of the other player.
	# Note that history may be empty!

	T = history.shape[1]
	if T==0:
		choice = np.random.randint(2)
	else:
		if np.random.rand() < 0.1:
			choice = np.random.randint(2)
		else:
			choice = history[0,T-1]
	

	return choice