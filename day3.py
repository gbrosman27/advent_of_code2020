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
                

# start at index 0 of first line.
# go to next line index 3 and record if tree
# go to next line index 6 and record if tree
# go to next line index 9 and record if tree

# keep dropping line and add 3 to the index. check if tree and add to counter. 
# if end of line reached, repeat from index 0 of next line.


            # Counts the trees in each line.
            # tree_counter = sled_run.count('#')               
            # print(tree_counter)
                

tree_finder()