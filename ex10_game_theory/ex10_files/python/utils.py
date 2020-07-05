import numpy as np


def single_trading_trial(choice1,choice2):
# choice1: player 1 choice (0 - Low, 1 - High)
# choice2: player 2 choice (0 - Low, 1 - High)
# return: payoff player 1, payoff player 2

	p1_payoff = np.array([[4,8],
						  [10,5]])

	p2_payoff = np.array([[4,10],
						  [8,5]])

	return p1_payoff[choice1, choice2], p2_payoff[choice1, choice2]


def run_game(merchant_1, merchant_2):
	# merchant_1 and merchant_2 are names of
	# 2 strategies (e.g., 'Merchant_00000001' and
	# 'Merchant_00000002') given as strings. This function will run them for
	# 1000 turns against each other and will report the payoffs of each one

	N = 1000
	payoffs = np.zeros((N,2));

	module_1 = __import__(merchant_1)
	module_2 = __import__(merchant_2)


	choices_p1 = []
	choices_p2 = []

	f_p1 = getattr(module_1, merchant_1)
	f_p2 = getattr(module_2, merchant_2)

	for i in range(N):
		history1 = np.stack((choices_p1, choices_p2))
		history2 = np.stack((choices_p2, choices_p1))

		p1_choice = f_p1(history1)
		p2_choice = f_p2(history2)

		payoffs[i,:] = single_trading_trial(p1_choice, p2_choice)

		choices_p1.append(p1_choice)
		choices_p2.append(p2_choice)

	u1 = np.mean(payoffs[:,0])
	u2 = np.mean(payoffs[:,1])

	return u1,u2
