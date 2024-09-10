def smallest_odd_k(target):
    n = 1
    # Start summing odd numbers
    current_sum = 0
    while current_sum < target:
        current_odd = 2 * n - 1  # The nth odd number is 2n - 1
        current_sum += current_odd
        print(f"Adding {current_odd}, cumulative sum is {current_sum}")
        n += 1
    
    # Once the sum >= target, return the last odd number added
    return current_odd

# Input target
target = 100
result = smallest_odd_k(target)
print(f"The smallest k such that the sum of odd numbers is >= {target} is: {result}")