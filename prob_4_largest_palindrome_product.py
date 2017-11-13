
def is_palindrome(number):
    num_str = str(number)
    corr_idx = len(num_str) - 1
    iter_range = int(len(num_str)/2)
    result = True

    for idx in range(iter_range):
        if not num_str[idx] == num_str[corr_idx]:
            result = False
            break
        corr_idx = corr_idx - 1

    return result    
        

NUMBER = 1000
largest_palindrome = -1

for i in range(100,NUMBER):
    for j in range(100,i+1):
        prod = i*j
        if is_palindrome(prod) and prod > largest_palindrome:
            largest_palindrome = prod

print largest_palindrome
