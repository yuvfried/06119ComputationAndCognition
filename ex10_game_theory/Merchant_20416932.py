import numpy as np


def Merchant_20416932(history):
    # Returns choice of 0 or 1
    # 0 - Low
    # 1 - High
    # history is aan array of 2xN previous choices:
    # the upper row is the previous choices of the player,
    # and the lower row is the previous choices of the other player.
    # Note that history may be empty!

    history = np.where(history == 0, -1, history)
    T = history.shape[1]
    if T == 0:
        return np.random.randint(2)

    scores = []
    for i in range(1, T):
        seq = history[1, i:][(history[0] == history[0, T - i])[:-i]]
        if len(seq) > 0:  # sequence which appears for the first time won't be calculated
            w = (0.5**i)
            mean_response = np.mean(seq)
            score = w * mean_response
            scores.append(score)

    response = np.sign(np.mean(scores))
    choice = int(response == -1)

    return choice
