def largest_even_k(target):
    n = 1
    current_sum = 0
    while True:
        current_even = 2 * (n - 1)  # The nth even number is 2*(n-1)
        if current_sum + current_even >= target:
            break
        current_sum += current_even
        print(f"Adding {current_even}, cumulative sum is {current_sum}")
        n += 1
    
    # The last valid even number added before exceeding the target
    return 2 * (n - 2)

# Input target
target = 25
result = largest_even_k(target)
print(f"The largest k such that the sum of even numbers is < {target} is: {result}")
