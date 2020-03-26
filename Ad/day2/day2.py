import itertools as it
input_arr = [1,2,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0]
# input_arr = [1, 1, 1, 4, 99, 5, 6, 0, 99]

# print("Day 2: part 1")

# input_arr[1] = 12
# input_arr[2] = 2


def process_array(input_arr):
    arr = input_arr[:]
    index = 0
    while index < len(arr):
        if arr[index] == 99:
            # print("STOP: OPCODE=99")
            break
        elif arr[index] == 1:
            # print("OPCODE=1")
            arr[arr[index + 3]] = arr[arr[index + 1]] + arr[arr[index + 2]]
            index += 4
        elif arr[index] == 2:
            # print("OPCODE=2")
            arr[arr[index + 3]] = arr[arr[index + 1]] * arr[arr[index + 2]]
            index += 4

    return arr[0]

print(process_array(input_arr))

print("Day 2: part 2")

nouns = list(range(1,100))
verbs = list(range(1,100))
for noun in nouns:
    input_arr[1]=noun
for verb in verbs:
    input_arr[2]=verb

for combo in it.product(nouns, verbs):
    input_arr[1] = combo[0]
    input_arr[2] = combo[1]
    if process_array(input_arr) == 19690720:
        print(combo[0]*100+combo[1])

