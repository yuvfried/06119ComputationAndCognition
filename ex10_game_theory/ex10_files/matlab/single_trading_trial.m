function [payoff] = single_trading_trial(choice1,choice2)
% choice1: player 1 choice (0 - Low, 1 - High)
% choice2: player 2 choice (0 - Low, 1 - High)
% return: payoff(1) -- player 1 payoff, payoff(2) player 2 payoff

p1_payoff = [4 8;
    		 10 5];

p2_payoff = [4 10;
    		 8 5];

payoff = [p1_payoff(choice1+1,choice2+1), p2_payoff(choice1+1,choice2+1)];


end