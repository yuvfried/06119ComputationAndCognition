function [choice] = Merchant_00000001(history)
% Returns choice of 0 or 1
% 0 - Low
% 1 - High
% history is a vector of 2xN previous choices:
% the upper row is the previous choices of the player,
% and the lower row is the previous choices of the other player.
% Note that history may be empty!

    if isempty(history)
        choice = randi(2)-1;
    else
        choice = 1-history(1,end);
    end

end