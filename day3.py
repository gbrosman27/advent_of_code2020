def tree_finder():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day3_input.txt', 'r') as data:
        # For each line in the data file, append the line as a string into the input_list.
        input_list = [line.rstrip('\n') for line in data]


        # Initialize variables
        sled_run = []
        index = 0
        tree_counter = 0


        # For the length of the input list, expand each line to allow the loop to 
        # run all the way through to the bottom.
        for i in range(len(input_list)):
            sled_run.append(input_list[i] * 32)


        # If the index on the current line is a '#' increment the tree_counter variable by 1. 
        # Add 3 to the current index and check for tree on next line.
        for line in sled_run:
            if line[index] == '#':
                tree_counter += 1
            index += 3

    
        return tree_counter
                                

print(tree_finder())
# Answer = 209