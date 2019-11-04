#solution to problem 0 of task
from string import ascii_lowercase #importing required library
n=int(input())   #taking input the size
total_width = 4*n - 3  #calculated width for that size
str = ascii_lowercase[:n]
str = str[::-1] + str[1:]
#printing pattern
for c in str:
    t = str[:str.index(c)]
    t = '-'.join(t + c + t[::-1])
    dashes = (total_width - len(t)) // 2 * '-'
    print(dashes + t + dashes)
