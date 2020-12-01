def expense_report():
    # Get and read the data file from the txt and make it the data variable
    with open('data_files/day1_input.txt', 'r') as data:
        # Convert the data inputs to ints and drop the '\n' symbol. Store as a list of ints.
        data_list = [int(line.rstrip('\n')) for line in data]


        # Nested for loops add numbers until a combination equals 2020.
        # Have each list start at the appropriate value by slicing. 
        # Then multiply those values and return the total.
        for i in data_list:
            for j in data_list[1:]:
                for x in data_list[2:]:
                    if i + j + x == 2020:          
                        return i * j * x
             
        
print(expense_report())


# ...Specifically, they need you to find the two entries that sum to 2020 and then multiply 
# those two numbers together.

# For example, suppose your expense report contained the following:

# 1721
# 979
# 366
# 299
# 675
# 1456
# In this list, the two entries that sum to 2020 are 1721 and 299. 
# Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

# Of course, your expense report is much larger. Find the two entries that sum to 2020; 
# what do you get if you multiply them together? How about three entries?