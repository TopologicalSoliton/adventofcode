

input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0]
output = 19690720
# output = [3500,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50]
def Intcode(code):

    for i in range(0, len(code), 4):

        if code[i] == 1:
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
        elif code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
        elif code[i] == 99:
            return code

    return code


def find_output(code, out):

    for i in range(0,100):
        for j in range(0,100):
            _code = code[:]
            _code[1] = i
            _code[2] = j
            if Intcode(_code)[0] == output:
                return i,j



noun, verb = find_output(input, output)
print(100*noun + verb)
