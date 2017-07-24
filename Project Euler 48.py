def power_up(number, exponent):
    return (number ** exponent)

def add_powers(max_num):
    sum_powers = 0
    for n in range(1, max_num + 1):
        sum_powers += power_up(n, n)
        n += 1
    return sum_powers

#returns the last num_of_digits from number
def last_digits(number, num_of_digits):
    str_number = str(number)
    return str_number[-num_of_digits:]

def last_sum_powers(x, last_nums):
    sum_powers = add_powers(x)
    return last_digits(sum_powers, last_nums)

print(last_sum_powers(1000, 10))
