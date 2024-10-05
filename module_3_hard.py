data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*i):
    first = i[0]
    sum_ = 0
    if type(first) == list:
        for n in first:
            sum_ += int(n)
    elif type(first) == dict:
        for key, value in first.items():
            sum_ += len(key) + int(value)
    elif type(first) == tuple:
        for l in first:
            if type(l) == int:
                sum_ += l
            elif type(l) == dict:
                for key, value in l.items():
                    sum_ += len(key) + int(value)
    elif type(first) == str:
        sum_ += len(first)
        pass
    print(first)
    return sum_ + calculate_structure_sum(*i[1:])


result = calculate_structure_sum(*data_structure)
print(result)








