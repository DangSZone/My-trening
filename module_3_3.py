n = 0
def calls():
    global n
    n += 1
    a = '------',n,'------'
    print(*a)
    
def print_params(a = 1, b = 'string', c = True):
    calls()
    print(a, b, c)




print_params() # 1
print_params(2, list([1,2,3]), False) # 2
print_params(b = 25) # 3
print_params(c = [1,2,3]) # 4

values_list = ['Canada', 4.20, True]
values_dict = {'a': False, 'b':'Free', 'c': 404}

print_params(*values_list) # 5
print_params(**values_dict) # 6

values_list2 = [0, True]
print_params(*values_list2, c="zero") # 7