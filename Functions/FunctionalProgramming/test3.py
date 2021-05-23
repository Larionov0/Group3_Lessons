def gen1(*strings):
    i = 0
    while i < len(strings[0]):
        word = ''
        for string in strings:
            word += string[i]
        yield word
        i += 1


for w in gen1('abc', 'cde', 'lol', 'kek'):
    print(w)
