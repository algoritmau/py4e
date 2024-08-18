# Solution

# Sum: The sum of all the numbers in the provided file is 489,284.

import re

# Path to the uploaded file - You might to adjust it to run it locally
file_path = '/mnt/data/regex_sum_2046812.txt'

# Initialize a sum variable
total_sum = 0

# Read the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Find all numbers in the line using regular expressions
        numbers = re.findall(r'[0-9]+', line)
        # Convert each found number to an integer and add to the total sum
        total_sum += sum(map(int, numbers))

total_sum
