def add_powers(max_num):
    sum_powers = 0
    for n in range(1, max_num + 1):
        sum_powers += (n ** n)
        n += 1
    return sum_powers

def last_digits(number, num_of_digits):
    str_number = str(add_powers(number))
    return str_number[-num_of_digits:]

print(last_digits(1000, 10))
