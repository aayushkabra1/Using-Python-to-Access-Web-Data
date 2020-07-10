import re

sum = 0

with open("D:\coursera\python\\test.txt") as f:
    reader = f.read()
    ls = re.findall("[0-9]+", reader)

    for num in ls:
        sum += int(num)

print(sum)        