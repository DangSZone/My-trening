from operator import truediv

calls = 0
def count_call():
    global calls
    calls += 1
def string_info(string):
    count_call()
    string = str(string)
    n = (len(string), string.upper(),string.lower())
    return n
def is_contains(string,list_to_search):
    count_call()
    string = str(string.upper())
    n = [j.upper() for j in list_to_search]
    if string in n:
        m = True
    else:
        m = False
    return m
print(string_info("Tiger"))
print(string_info('Dog and cat'))
print(string_info("SaTaNa"))
print(is_contains('Love',['World','People']))
print(is_contains('Love', ['Jamaika', 'Canada','Holland','Child','lOvE']))
print(calls)