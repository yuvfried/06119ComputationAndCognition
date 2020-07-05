function [ u1, u2 ] = run_game( merchant_1, merchant_2 )
% merchant_1 and merchant_2 are names of
% 2 strategies (e.g., 'Merchant_00000001' and
% 'Merchant_00000002') given as strings. This function will run them for
% 1000 turns against each other and will report the payoffs of each one

N = 1000 ;
payoffs = zeros(N,2);

choices_p1 = [];
choices_p2 = [];
    
f_p1 = str2func(merchant_1);
f_p2 = str2func(merchant_2);
    
for i = 1:N

    history1 = [choices_p1; choices_p2];
    history2 = [choices_p2; choices_p1];
    
    p1_choice = f_p1(history1);
    p2_choice = f_p2(history2);
    
    payoffs(i,:) = single_trading_trial(p1_choice, p2_choice);

    choices_p1(i) = p1_choice;
    choices_p2(i) = p2_choice;
    
    
end

u1 = mean(payoffs(:,1));
u2 = mean(payoffs(:,2));

end


