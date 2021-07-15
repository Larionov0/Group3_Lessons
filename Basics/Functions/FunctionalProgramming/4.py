def get_last_letter(word):
    return word[-1]


words = ['бульба', "корова", "ананас", "зелений"]

new_list = list(map(get_last_letter, words))
# new_list = [get_last_letter(word) for word in words]

print(new_list)
