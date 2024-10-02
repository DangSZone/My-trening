def single_root_words(root_words = '' , *other_words):
    root_words = root_words.upper()
    same_words = []
    for n in other_words:
        b = n.upper()
        if root_words in b:
            same_words.append(n)
        if b in root_words:
            same_words.append(n)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)