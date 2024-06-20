#!/usr/bin/python3
""" Prime Game """


def is_prime(number):
    """ A function to decide if the number is prime or not """
    if number <= 1:
        return False
    elif number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """ Is winner function """

    maria_counter = 0
    ben_counter = 0

    while len(nums) != 0:
        round_array = [i for i in range(1, nums[0] + 1)]
        primes = []
        for number in range(nums[0]):
            if is_prime(number):
                primes.append(number)

        nums.pop(0)
        primes_copy = primes[:]
        accessed = True
        maria = True

        while accessed is True and len(primes_copy) != 0:
            starting_number = primes_copy.pop(0)
            accessed = False
            while(starting_number <= round_array[-1]):
                if round_array[starting_number - 1] != 0:
                    round_array[starting_number - 1] = 0
                    accessed = True
                starting_number *= 2
            if accessed is True:
                maria = not maria

        if (maria is True):
            ben_counter += 1
        else:
            maria_counter += 1

    if ben_counter > maria_counter:
        return "Ben"
    elif maria_counter > ben_counter:
        return "Maria"
    return None