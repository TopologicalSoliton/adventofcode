import os
import sys
import numpy as np

data = np.loadtxt('input.txt')


# make a list with all divided down values, then check that list, if any numbers above zero, do the same until all zero
def dividedown(x):
    return np.floor(x / 3) - 2


divlist1 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in data]
divlist2 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist1]
divlist3 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist2]
divlist4 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist3]
divlist5 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist4]
divlist6 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist5]
divlist7 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist6]
divlist8 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist7]
divlist9 = [0 if dividedown(number) < 0 else dividedown(number)
            for number in divlist8]
divlist10 = [0 if dividedown(number) < 0 else dividedown(number)
             for number in divlist9]
divmatrix = [
    divlist1,
    divlist2,
    divlist3,
    divlist4,
    divlist5,
    divlist6,
    divlist7,
    divlist8,
    divlist9
]
totallist = []
for row in divmatrix:
    for col in row:
        totallist.append(col)
answer = np.sum(totallist)
print(divlist10, answer)


# print(divlist1, divlist2)


# [[i*j for j in range(1,11)] for i in range(7,9)]
# list1 = [np.floor(number / 3) - 2 for number in data]
# list2 = [np.floor(number / 3) - 2 for number in list1]
# list3 = [np.floor(number / 3) - 2 for number in list2]
# list4 = [np.floor(number / 3) - 2 for number in list3]
# list5 = [np.floor(number / 3) - 2 for number in list4]
# list6 = [np.floor(number / 3) - 2 for number in list5]
# list7 = [np.floor(number / 3) - 2 for number in list6]
# list8 = [np.floor(number / 3) - 2 for number in list7]
# list9 = [np.floor(number / 3) - 2 for number in list8]
# list10 = [0 if np.floor(i / 3) - 2 < 0 else np.floor(i / 3) - 2 for i in list9]
# # print(list1, list2, list3, list4, list5, list6, list7, list8, list9)
# print(list10)
