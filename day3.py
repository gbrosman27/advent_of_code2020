def tree_finder():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day3_input.txt', 'r') as data:
        # For each line in the data file, append the line as a string into the input_list.
        input_list = [line for line in data]

        # Initialize a counter to count the trees in the path.
        tree_counter = 0


        # For the length of the input list, split the data to get each line as its own list.
        for i in range(0, len(input_list)):
            sled_run = str(input_list[i].split())

            # Counts the trees in each line.
            tree_counter = sled_run.count('#')               
            print(tree_counter)
                

tree_finder()