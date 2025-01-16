# Use Markov chain to find the chance of getting 3 in a row in a coin toss experiment
import numpy as np
from numpy.linalg import matrix_power
def markov_chain_toss(pT=0.5, ntoss=10):
    """
    Use Markov transition matrix to calculate the probability of getting
    3 heads / tails in a row during <= ntoss tosses
    pT: probability of tails in 1 toss, fair coin assumption (pT = 0.5)
    ntoss: number of tosses in each experiment (ntoss = 10)
    """
    # transition matrix: tmatrix[row, column] == probability(from state, to state)
    # each row should sum up to 1
    tmatrix = np.array([
    # N    1H,   2H,   1T,   2T,   S
     [0,   1-pT, 0,    pT,   0,    0],     # From nothing (N)
     [0,   0,    1-pT, pT,   0,    0],     # From 1 heads (1H)
     [0,   0,    0,    pT,   0,    1-pT],  # From 2 heads (2H)
     [0,   1-pT, 0,    0,    pT,   0],     # From 1 tails (1T)
     [0,   1-pT, 0,    0,    0,    pT],    # From 2 tails (2T)
     [0,   0,    0,    0,    0,    1]      # From 3 in a row (S)
    ])

    final_state = matrix_power(tmatrix, ntoss)
    # return the probability of going from nothing (N) to achieving 3 in a row (S)
    return final_state[0, -1]


if __name__ == "__main__":
    pT = 0.5
    num_toss = 10
    res = markov_chain_toss(pT, num_toss)
    print(f"Checking the probability of getting 3 in a row using a coin with {pT} probability of getting tails, within {num_toss} coin tosses...")
    print(f"Markov chain gives probability {res}.")
