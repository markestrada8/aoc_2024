
# PART 1
def get_distance(lst_a, lst_b):
    return sum([abs(sorted(lst_a)[i] - sorted(lst_b)[i]) for i in range(len(lst_a))])

result = 0
with open('data.txt', 'r') as file:
    left = []
    right = []

    for line in file.readlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    result = get_distance(left, right)


print(result)


# PART 2
def find_similars(val, lst):
    return len([i for i in lst if i == val])

with open('data.txt', 'r') as file:
    left = []
    right = []

    for line in file.readlines():
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

    result = sum([num * find_similars(num, right) for num in left])

print(result)