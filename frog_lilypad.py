# Suppose a frog leaps across lily pads to get to the other side of the pond
# It can only leap 1 or 2 pads at a time. How many different ways can he leap over n lily pads?
# This turns out to be a Fibonacci series

def frog_lilypads(n, memo):
    """
    Use Fibonacci series to calculate the number of ways a frog can leap across n lily pads
    assuming it can only leap 1 or 2 pads at a time.
    n: total number of lily pads
    memo: memoization dictionary for speed-up.
    """
    if n < 1:
        memo[n] = 0
        return 0
    if n == 1:
        memo[n] = 1
        return 1
    if n == 2:
        memo[n] = 2
        return 2

    if n not in memo.keys():
        memo[n] = frog_lilypads(n-1, memo) + frog_lilypads(n-2, memo)

    return memo[n]

if __name__ == "__main__":
    memo = {}
    num_lilypads = 10
    num_paths = frog_lilypads(num_lilypads, memo)
    print(f"I'm a little frog living in the pond ")
    print(f"leaping on the lily pads")
    print(f"croaking 'to infinity and beyond'!")
    print(f"Two lily pads is the furthest I can hop")
    print(f"after {num_lilypads} pads I will stop.")
    print(f"How many ways can you count ")
    print(f"my lily pad leaps across the pond?")
    print(f"")
    print(f"One pad, two pads are all you can do.")
    print(f"There're {num_paths} paths to get you through!")