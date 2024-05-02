#!/usr/bin/python3
""" making change """

def makeChange(coins, total):
    """ Make change """

    if not coins or coins is None:
        return -1

    if total <= 0:
        return 0

    memo = [float('inf')] * (total + 1)
    memo[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0 and memo[i - coin] != float('inf'):
                memo[i] = min(memo[i], memo[i - coin] + 1)

    if (memo[total] == float('inf')):
        return -1
    return memo[total]

