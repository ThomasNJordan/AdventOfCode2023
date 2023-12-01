'''
Author: Thomas Jordan
Description: Day 1 tasked me with finding the first and last digits in a line of text, 
and combinging them to find the coordinates of a star.
'''

f = open("day1.txt", "r")
for line in f:
    totalSum = 0

    with open("day1.txt", "r") as f:
        for line in f:
            digits = [int(c) for c in line if c.isdigit()]
            totalSum += int(str(digits[0]) + str(digits[-1]))

print(f"Part 1: {totalSum}")

f = open("day1.txt", "r")
for line in f:
    totalSum = 0

    # the reason the first and last letter of the original have to stay is 
    # there are cases where two numbers share a letter so this gaurentees 
    # that both letters get parsed 
    num_words = { 
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    with open("day1.txt", "r") as f:
        for line in f:
            # Convert words to digits
            for word, i in num_words.items():
                line = line.replace(word, i)

            # Same program as part 1
            digits = [int(c) for c in line if c.isdigit()]
            totalSum += int(str(digits[0]) + str(digits[-1]))

print(f"Part 2: {totalSum}")