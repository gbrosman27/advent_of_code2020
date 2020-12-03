def tree_finder():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day3_input.txt', 'r') as data:
        # For each line in the data file, append the line as a string into the input_list.
        input_list = [line for line in data]

        # Initialize a counter to count the trees in the path.
        tree_counter = 0


        # For the length of the input list, split the data to get each line as its own list.
        for i in range(0, len(input_list)):
            sled_run = input_list[i].split()[0]
            print(sled_run)

# start at index 0 of first line.
# go to next line index 3 and record if tree
# go to next line index 6 and record if tree
# go to next line index 9 and record if tree

# keep dropping line and add 3 to the index. check if tree and add to counter. 
# if end of line reached, repeat from index 0 of next line.


            # Counts the trees in each line.
            tree_counter = sled_run.count('#')               
            print(tree_counter)
                

tree_finder()