#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])  # 100
    capacity = int(firstLine[1])  # 100000

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    # import ipdb; ipdb.set_trace()
    value = 0
    weight = 0
    taken = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))  # Wow !!! map(str, integers)
    return output_data

def traceback_matrix(matrix):
    takens = [0] * (len(matrix[0]) - 1)



def dp(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])  # 100
    capacity = int(firstLine[1])  # 100000

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    taken = [0] * len(items)
    capacity_item = [[0 for _ in range(item_count+1)] for _ in range(capacity+1)]
    for j in range(item_count):
        for k in range(capacity):
            if items[j].weight <= k+1:
                capacity_item[k+1][j+1] = max(
                    capacity_item[k+1][j], items[j].value + capacity_item[k+1-items[j].weight][j])
            else:
                capacity_item[k+1][j+1] = capacity_item[k+1][j]
    for ele in capacity_item:
        print ele

    optim_value = capacity_item[-1][-1]
    # prepare the solution in the specified output format
    output_data = str(optim_value) + ' ' + str(1) + '\n'
    output_data += ' '.join(map(str, taken))  # Wow !!! map(str, integers)
    return output_data

def test_dp():
    input_data = "4 7\n16 2\n19 3\n23 4\n28 5"
    print dp(input_data)


if __name__ == '__main__':
    test_dp()
    raise Exception("")
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        # print(solve_it(input_data))
        print(dp(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

