import sys

N = int(sys.stdin.readline())

color = list(map(str, sys.stdin.readline().rstrip()))

blue_start = 1
red_start = 1
blue_flag = True
red_flag = True

for c in color:
    if c == 'B':
        blue_flag = True

        if red_flag == True:
            red_flag = False
            red_start += 1
    else:
        if blue_flag == True:
            blue_flag = False
            blue_start += 1

        red_flag = True

print(min(blue_start, red_start))