# Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games? and sum them up to give you the answer
# the input is like this :
#     Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#     Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
#     Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
#     Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
#     Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# we have 100 game.
#log in and get your own puzzle input @ : https://adventofcode.com/2023/day/2/input
import re
file=open('./CP/input.txt','r')
summer=0 # the sum
data=file.readlines()
for line in data:
    noice=True
    r=re.findall(r'[0-9]{1,2} red', line)
    for i in r:
        if int(i.strip(' red'))>12:
            noice=False
            break
    if not noice : continue
    g=re.findall(r'[0-9]{1,2} green', line)
    for i in g:
        if int(i.strip(' green'))>13:
            noice=False
    if not noice : continue
    b=re.findall(r'[0-9]{1,2} blue', line)
    for i in b:
        if int(i.strip(' blue'))>14:
            noice=False
    if noice:
        summer+=int(re.findall(r'Game [0-9]{1,3}',line)[0].strip('Game '))
print(summer)
