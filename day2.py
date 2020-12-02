def password_policy():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day2_input.txt', 'r') as data:
 
        # For each line in the data file, append the line as a string into the input_list
        input_list = []
        for line in data:
            input_list.append(str(line))

        # Initialize valid password counter
        count = 0

        # For each item in the input list...
        for i in range(0,len(input_list)):
            # Split the list item into strings. Default is to split on whitespace.
            pwd_policy = input_list[i].split()

            # Initialize min, max, and letter variables
            min_num = 0
            max_num = 0
            letter = ''

            # Create list to hold the min and max values
            min_max_list = []
            
            # Split the first value of the pwd_policy list on the hyphen and save in the min_max_list.
            min_max_list = pwd_policy[0].split('-')
            print(min_max_list)
            min_num = int(min_max_list[0])
            max_num = int(min_max_list[1])

            letter = pwd_policy[1].split(':')[0]
            letter_count = pwd_policy[2].count(letter)
            
            #print(min_num, max_num, letter, pwd_policy[2], letter_count)

            if min_num <= letter_count <= max_num:
                count+=1
            #print(count)
            
        print(count) #Solution-1

password_policy()