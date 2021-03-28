file = open('myfile.txt', 'rt')

text = file.read(5)
print(text)
text = file.read(5)
print(text)
text = file.read()
print(text)

text = file.read()
print(text)

file.close()
