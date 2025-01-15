# Check the chance of getting 3 in a row in a coin toss problem using simulation.
# toss_simulation() --> coin_toss() gives the simulation results
import numpy as np

def coin_toss(pT=0.5, ntoss=10):
    """
    One run of ntoss tosses to see if we succeed (get 3 in a row at least once).
    pT: probability of tails, fair coin by default (pT = 0.5)
    ntoss: number of tosses in 1 simulation (ntoss = 10)
    """
    tosses = []
    for i in range(ntoss):
        toss = np.random.choice(['H', 'T'], p=[1-pT, pT])
        tosses.append(toss)
        if tosses[-3:] == ['H', 'H', 'H'] or tosses[-3:] == ['T', 'T', 'T']:
            return 1  # we managed to get 3 in a row in le ntoss tosses, 1 success
    return 0  # we didn't manage to get 3 in a row in le ntoss tosses, 0 success

def toss_simulation(nsimulation=10000, pT=0.5, ntoss=10):
    """
    Run coin_toss() nsimulation times (law of large numbers) to estimate the expectation.
    nsimulation: number of total simulations (nsimulation = 10,000)
    pT: probability of tails, fair coin assumption (pT = 0.5)
    ntoss: number of tosses in each simulation (ntoss = 10)
    """
    success = 0
    for j in range(nsimulation):
        success += coin_toss(pT, ntoss)

    success_prob = success / nsimulation
    return success_prob

if __name__ == "__main__":
    num_simul = 1000000
    num_toss = 10
    pT = 0.5
    res = toss_simulation(num_simul, pT, num_toss)
    print(f"Checking the probability of getting 3 in a row using a coin with {pT} probability of getting tails, within {num_toss} coin tosses...")
    print(f"{num_simul} simulation(s) give(s) probability {res}.")

