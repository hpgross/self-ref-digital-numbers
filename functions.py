def indexer(input_char):
    char_values={
        "0":1110111,
        "1":100100,
        "2":1011101,
        "3":1011011,
        "4":111010,
        "5":1101011,
        "6":1101111,
        "7":1010010,
        "8":1111111,
        "9":1111101
    }
    return char_values[input_char]

def next_num(cur_num):
    num_str = str(cur_num)
    while len(num_str) < 7:
        num_str = "0" + num_str
    counter = 0
    for character in num_str:
        counter += indexer(character)
    return counter
found_loops = []

def list_from_start(cur_num):
    num_list = [cur_num]
    next = next_num(cur_num)
    while next not in num_list:
        num_list.append(next)
        next = next_num(next)
    new_loop = True
    for item in found_loops:
        if next in item:
            new_loop = False
    if new_loop == True:
        found_loops.append(num_list[num_list.index(next):])
    num_list.append(next)
    return num_list

print(1)
for number in range(0,9999999):
    print(number)
    cur_list = list_from_start(number)

print(len(found_loops))
print(found_loops)