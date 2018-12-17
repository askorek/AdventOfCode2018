with open("day_05.txt") as f:
    data = f.read().strip()

# data = 'dabAcCaCBAcCcaDA'

def reduce_once(string_to_reduce):
    new_string = []
    skip_next = False
    for i in range(len(string_to_reduce) - 1):
        if skip_next:
            skip_next = False
            continue
        elif abs(ord(string_to_reduce[i]) - ord(string_to_reduce[i+1])) == 32:
            skip_next = True
            continue
        else:
            new_string.append(string_to_reduce[i])

    if not skip_next:  # adding last element

        new_string.append(string_to_reduce[-1])

    return ''.join(new_string)

def reduce_many_times(data):
    while True:
        new = reduce_once(data)
        if len(new) == len(data):
            break
        else:
            data = new
    return new

output = reduce_many_times(data)
print(len(output))

all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

min_len = 999999999

for letter in all_letters:
    print(letter)
    removed_data = data.replace(letter, '').replace(letter.lower(), '')
    reduced = reduce_many_times(removed_data)
    if len(reduced) < min_len:
        min_len = len(reduced)

print(min_len)