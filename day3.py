def tree_finder():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day3_input.txt', 'r') as data:
        # For each line in the data file, append the line as a string into the input_list.
        input_list = [line for line in data]

        # Initialize variables
        sled_run = []
        index = 0
        tree_counter = 0


        # For the length of the input list, split the data to get each line as its own list.
        for i in range(len(input_list)):
            sled_run.append(input_list[i].split()[0])

        for line in sled_run:
            if line[index] == '#':
                tree_counter += 1
            if index == len(line) - 1:
                index -= len(line) + 2
            else:
                index += 3

    
        print(tree_counter)
                                

tree_finder()
# 209

# with open('data_files/day3_input.txt') as file:
#     map = file.readlines()
#     map = [ line.strip() for line in map]


# treeCount = 0
# row, col = 0,0

# while row+1 < len(map):
#     row +=1
#     col +=3

#     space = map[row][col % len(map[row])]
#     if space == '#':
#         treeCount +=1

# print(treeCount)


# slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

# total = 1

# for slope in slopes:
#     treeCount=0
#     row, col = 0,0

#     while row+1 < len(map):
#         row += slope[1]
#         col += slope[0]

#         space = map[row][col % len(map[row])]
#         if space  == '#':
#             treeCount += 1

#     total *= treeCount

# print(total)