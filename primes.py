"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0 :
        raise ValueError('function cannot be ran on 0 or negative numbers')

    
    list = []
    testNumber = 1
    flag = False
    while len(list) < number_of_primes:
        testNumber+=1
        flag = False

        #as all numbers are comprised of prime factors, by checking our list of primes smaller then the
        #target number, if it is divisible by one of them, it is not prime.
        for prime in list:
            if testNumber % prime == 0:
                flag = True
                break

        if flag == False:
            list.append(testNumber)            

    return list

