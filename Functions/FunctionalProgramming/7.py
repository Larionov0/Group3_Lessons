words = ['бульба', "корова", "ананас", "зелений", 'качка']

new_words = filter(lambda word: 'а' in word, words)
# new_words2 = [word for word in words if 'а' in word]

print(list(new_words))
