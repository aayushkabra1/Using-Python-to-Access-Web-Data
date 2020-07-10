import re

with open("test.txt") as f:
    reader = f.read()
    nums = re.findall("[0-9]+", reader)
    
sum = 0    
for num in nums:
    int_num = int(num)
    sum += int_num

print(sum)    
