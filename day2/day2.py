'''
Author: Thomas Jordan
Code: Advent of Code: Day 2
'''
numRed = 12
numGreen = 13
numBlue = 14

totalWork = 0
lineNum = 1 # too lazy to parse for Game #

f = open("input.txt", "r")
for line in f:
    line = line.strip()
    lineList = []

    # Convert line to list
    for word in line:
        lineList.append(word)

    game_str, val_str = line.split(": ") # Game string | Values string
    game_valid = True
    for group in val_str.split("; "):
        for color_str in group.split(", "):
            num_str, color = color_str.split(" ")
            num = int(num_str)
            if color == 'red' and num > 12:
                game_valid = False
            if color == 'green' and num > 13:
                game_valid = False
            if color == 'blue' and num > 14:
                game_valid = False
    if game_valid:
        totalWork += lineNum

    lineList = [] # empty list for other operations
    lineNum += 1

print(totalWork)

''' Part 2 '''
colorpow = 0
f = open("input.txt", "r")
for line in f:
    maxRed = maxGreen = maxBlue = 0

    line = line.strip()
    lineList = []

    # Convert line to list
    for word in line:
        lineList.append(word)

    game_str, val_str = line.split(": ") # Game string | Values string
    for group in val_str.split("; "):
        for color_str in group.split(", "):
            num_str, color = color_str.split(" ")
            num = int(num_str)
            if color == 'red' and num > maxRed:
                maxRed = num
            if color == 'green' and num > maxGreen:
                maxGreen = num
            if color == 'blue' and num > maxBlue:
                maxBlue = num

    lineList = [] # empty list for other operations
    lineNum += 1
    colorpow += maxBlue * maxGreen * maxRed

print(colorpow)
