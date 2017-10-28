curr_even_sum = 0
curr_num = 2
prev_num = 1

while curr_num < 4000000:
    if (curr_num % 2 == 0):
        curr_even_sum = curr_even_sum + curr_num

    next_num = curr_num + prev_num
    prev_num = curr_num
    curr_num = next_num

print ("prev_num = ", prev_num)
print ("curr_even_sum = ", curr_even_sum)
