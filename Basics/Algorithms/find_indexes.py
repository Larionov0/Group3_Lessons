string = 'I hate yourself. I love myself.elf'
substring = 'elf'

intervals = []

i = 0
while i < len(string) - len(substring) + 1:
    if string[i:i + len(substring)] == substring:
        intervals.append([i, i + len(substring) - 1])
    i += 1

print(string)
subline = ''
i = 0
while i < len(string):
    result = False
    for interval in intervals:
        if interval[0] <= i <= interval[1]:
            subline += '-'
            result = True
            break

    if result is False:
        subline += ' '
    i += 1
print(subline)

