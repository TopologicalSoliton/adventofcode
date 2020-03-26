min = 147981
max = 691423

def is_candidate(x):
    # count the num of pairs per number:
    doubles = [0,0,0,0,0,0,0,0,0,0]

    for i in range(5,0,-1):
        j = i - 1

        former = int((x % 10**(i+1) - x % 10**i) / 10**i)
        latter = int((x % 10**(j+1) - x % 10**j) / 10**j)

        if former == latter:
            doubles[former] += 1
        if former > latter:
            return False
    # if there exists a number x for which only one pair is found:
    # alternatively: (doubles[x] == 1)
    return True and (1 in doubles)

def find_num_candidates(min, max):
    counter = 0
    for i in range(min, max):
        if is_candidate(i):
            counter += 1
    return counter

print(find_num_candidates(min,max))
