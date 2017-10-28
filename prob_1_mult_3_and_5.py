sum_mult = []
BELOW_ = 1000

curr_sum = 0
for i in range(BELOW_):
    if (i % 3 == 0) or (i % 5 == 0):
        curr_sum = curr_sum + i

    sum_mult.append(curr_sum)

print "printing sum of mult 3 and 5 for numbers below 10"
print sum_mult[10 - 1]

print "printing sum of mult 3 and 5 for numbers below 1000"
print sum_mult[BELOW_ - 1]
