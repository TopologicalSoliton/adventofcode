
# # save all positions, cross-ref where the same, calc distance, pick shortest
# # save pos (x,y)
# # recognize commands, if first letter of input = L/R/D/U then -x/+x/-y/+y

# import numpy as np

# data = np.loadtxt("input.txt", dtype=str, delimiter=",")
# moving_input_1 = data[0]
# moving_input_2 = data[1]


# def populate_grid(moving_input):
#     coordinates = []

#     # Set the current position
#     x, y = (0, 0)

#     # Loop through all the directions
#     for instruction in moving_input:
#         direction = instruction[0]
#         distance = int(instruction[1:])

#         move_x = move_y = 0

#         if direction == "L":
#             move_x = -1
#         if direction == "R":
#             move_x = 1
#         if direction == "D":
#             move_y = -1
#         if direction == "U":
#             move_y = 1

#         for _ in range(0, distance):
#             x += move_x
#             y += move_y
#             new_coordinate = (x, y)

#             coordinates.append(new_coordinate)

#     return coordinates


# def min_distance(input_1, input_2):

#     distances = []
#     intersections = list(set(input_1).intersection(input_2))
#     for intersection in intersections:
#         distance = abs(intersection[0]) + abs(intersection[1])
#         distances.append(distance)
#     # return min(distances)
#     return distances


# def shortest_path(input_1, input_2):
#     distances = []
#     intersections = list(set(input_1).intersection(input_2))
#     for intersection in intersections:
#         distances.append(intersection)
#         # (x,y) = (intersection[0],intersection[1])
#         # xs.append(x)
#         # ys.append(y)
#     # return min(distances)
#     return distances


# intersections = list(set(moving_input_1).intersection(moving_input_2))
# wires = []
# wire_1 = populate_grid(moving_input_1)
# wire_2 = populate_grid(moving_input_2)
# wires.append(wire_1)
# wires.append(wire_2)
# # print(sum(wire_1.index(intersect)))
# # print(wire_1)
# # wire_2 = populate_grid(moving_input_2)
# # print(list(set(wire_1).intersection(wire_2)))
# # print("SOLUTION is", min_distance(wire_1, wire_2))
# # wire_1 = populate_grid(moving_input_1)
# # wire_2 = populate_grid(moving_input_2)
print()
# print(min(sum(wire_1.index(intersect))
#           for intersect in intersections))  # Part 2


def process_wire(instr_line):
    current_pos = [0, 0]
    for instr in instr_line.split(','):
        for _ in range(int(instr[1:])):
            current_pos[0 if instr[0] in (
                'L', 'R') else 1] += -1 if instr[0] in ('L', 'D') else 1
            yield tuple(current_pos)


with open('input.txt', 'r') as f:
    wires = [list(process_wire(line)) for line in f.readlines()]

intersections = set(wires[0]) & set(wires[1])
print
print(min(abs(x) + abs(y) for (x, y) in intersections))  # Part 1
print(2 + min(sum(wire.index(intersect) for wire in wires)
              for intersect in intersections))  # Part 2
