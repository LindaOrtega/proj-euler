import sys
import math

# Determines if num is in form of a prime
# All prime numbers, except 2 and 3, are in the form 6k +- 1
def in_prime_format(num):
    mod_plus = (num + 1) % 6
    mod_minus = (num - 1) % 6
    if (num == 2) or (num == 3):
        return True
    elif (mod_plus == 0) or (mod_minus == 0):
        return True
    else:
        return False

# Determines primality of num through brute force of 
# all m in range of 2 and sqrt(num) + 1 that are in prime format.
def is_prime(num):
    sqrt_n  = int(math.sqrt(num))
    result = True

    for i in range(2, sqrt_n + 1):
        if in_prime_format(i) and (num % i == 0):
            result = False
            break
    
    return result

NUMBER_ = int(sys.argv[1])
upper_range = int(math.sqrt(NUMBER_))
fst_factors = []
scd_factors = []
largest_prime = -1


# Make list of potentially prime factors from largest to biggest
for fst in range(2,upper_range + 1):
    if NUMBER_ % fst == 0:
        scd = NUMBER_ / fst
        if in_prime_format(fst): 
            fst_factors.append(fst)
        if in_prime_format(scd):
            scd_factors.append(scd)

print ("fst_factors = ", fst_factors)
print ("scd_factors = ", scd_factors)

# Determine primality of factors, starting with largest.
# Note: scd_factors >= fst_factors
if fst_factors:                     
    for f in scd_factors:           # first element is the largests
        if is_prime(f):
            largest_prime = f
            break
        
    if largest_prime == -1:         # None of scd_factors were prime
        # Determine primality 
        while fst_factors:          # last element is the largest
            f = fst_factors.pop()
            if is_prime(f):
                largest_prime = f
                break 

    if largest_prime == -1:         # None of fst_factors were prime
        largest_prime = NUMBER_       

else:                               # Has no factors and is prime.
    largest_prime = NUMBER_ 

print NUMBER_
print largest_prime

"""
# Create Sieve of Eratosthenes method table
mult_table = [False] * (upper_range/2 + 1)

for i in range(2, upper_range/2):
    if not mult_table[i]:
        for m in range(2,upper_range/2):
            prod = i * m
            if prod > upper_range:
                break
            else:
                if (prod <= upper_range/2) and (not mult_table[prod]):
                    mult_table[prod] = True
"""
