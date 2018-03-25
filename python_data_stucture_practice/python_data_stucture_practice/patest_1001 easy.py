
'''
Calculate a + b and output the sum in standard format -- that is, the digits must be separated into groups of three by commas (unless there are less than four digits).

Input

Each input file contains one test case. Each case contains a pair of integers a and b where -1000000 <= a, b <= 1000000. The numbers are separated by a space.

Output

For each test case, you should output the sum of a and b in one line. The sum must be written in the standard format.

Sample Input
-1000000 9
Sample Output
-999,991
'''

#a = int(input("a = "))
#b = int(input("b = "))

def do_something(a,b):
    c = a+b
    format(c)


def format(num):
    if num > -10000 and num < 10000:
        print(num)
    else:
        #-999,999 or 999,999 
        print('{:,}'.format(num))

test= [[100000,-1000],[100000,-1],[-100000,1]]
for t in test:
    a = t[0]
    b = t[1]
    print (a,b)
    print('/')
    do_something(a,b)

