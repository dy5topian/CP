# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# the goal is to calculate last and first character
## url to the file : https://adventofcode.com/2023/day/1/input
filer='0123456789'
summer=0
Input=open('input.txt','r')
data=Input.readlines()
for String in data:
    nub=''
    for sub in String:
        if sub in filer:
            nub+=sub
    if len(nub)==1:
        summer+=int(nub*2)
    else:
        summer+=int(nub[0]+nub[-1])
print(summer)



