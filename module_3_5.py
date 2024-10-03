def get_multiplied_digits(number):
    str_numbers = str(number)
    first = int(str_numbers[0])
    if first == 0:
        first = 1
    if len(str_numbers) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_numbers[1:]))

print(get_multiplied_digits(40203))
print('------')
print(get_multiplied_digits(420100000))
print(get_multiplied_digits(7))