elfs = []
with open('input.txt', 'r') as reader:
    line = reader.readline()

    elfs.append(0)
    while line != '':
        if line == '\n':
            elfs.append(0)
        else:
            elfs[-1] = elfs[-1] + int(line)

        line = reader.readline()

fatboys = [0,0,0]
for elf in elfs:
    if elf > fatboys[0]:
        if elf > fatboys[1]:
            if elf > fatboys[2]:
                fatboys[0] = fatboys[1]
                fatboys[1] = fatboys[2]
                fatboys[2] = elf
            else:
                fatboys[0] = fatboys[1]
                fatboys[1] = elf
        else:
            fatboys[0] = elf




print(fatboys)
total = 0
for fatboy in fatboys:
    total += fatboy

print(total)