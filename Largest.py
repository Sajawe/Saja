def largestnumber(numbers):

    biggest_num =numbers[0]

    for num in numbers:
        if num > biggest_num:
            biggest_num = num

    return biggest_num


print(largestnumber([23,46,-11]))