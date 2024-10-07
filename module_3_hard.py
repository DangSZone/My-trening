

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_ = 0
def calculate_structure_sum(*i):
    global sum_
    for el in i:
        if isinstance(el,(list,tuple)):
           calculate_structure_sum(*el)
        elif isinstance(el, dict):
            for k in el.items():
                calculate_structure_sum(k)
        elif isinstance(el, int):
            sum_ += el
        elif isinstance(el, str):
            sum_ += (len(el))
        else:
            calculate_structure_sum(*el)
    return sum_



print(calculate_structure_sum(data_structure))









