def is_candidate(id):
    return not len(id) == len(set(id))

def has_nths(id, n):
    for letter in id:
        if id.count(letter) == n:
            return True
    return False

with open("day_02.txt") as f:
    data = f.readlines()

twos = 0
tres = 0

for line in data:
    if is_candidate(line):
        if has_nths(line, 2):
            twos += 1
        if has_nths(line, 3):
            tres += 1
print(twos*tres)

# ----- PART 2 ---------

def count_difs(str1, str2):
    diffs = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diffs += 1
    return diffs

num_of_str = len(data)

def find_common(str1, str2):
    common = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            common += str1[i]
    return common

for i in range(len(data)):
    for j in range(i, len(data)):
        if count_difs(data[i], data[j]) == 1:
            print(find_common(data[i], data[j]))
