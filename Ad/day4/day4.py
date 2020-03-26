min = 264360
max = 746325


def is_candidate(x):
    doubles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(5, 0, -1):
        j = i - 1

        former = int((x % 10**(i + 1) - x % 10**i) / 10**i)
        latter = int((x % 10**(j + 1) - x % 10**j) / 10**j)
        # if former == latter:
        #     double = True
        if former == latter:
            doubles[former] += 1

        if former > latter:
            return False
    return True and (1 in doubles)


def num_candidates(min, max):
    counter = 0
    for i in range(min, max):
        if is_candidate(i):
            counter += 1
    return counter


print(num_candidates(min, max))
