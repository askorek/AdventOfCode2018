with open("day_01.txt") as f:
    data = f.readlines()

result = 0

for line in data:
        result += int(line)
print(f"result of summation is {result}")


###  ---- PART 2 ---- ###
import sys

freq_set = set()
result = 0
passing = 0
while True:
    for line in data:
        result += int(line)
        if result not in freq_set:
            freq_set.add(result)
        else:
            print(f"found: {result}")
            sys.exit()
        passing += 1
        print(f"passing nth time: {passing}")