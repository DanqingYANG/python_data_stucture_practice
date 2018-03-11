'''
Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.
exp. 
input:   "abc"
output: "cba"
'''

class stack1:
    def __init__(self):
        self.data = []

    def __push__(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def isEmpty(self):
        return self.data == []


def reverse1(s):
    a_stack = stack1()
    reverse_a_stack = ""
    for i in s:
        a_stack.__push__(i)
    while not a_stack.isEmpty():
        reverse_a_stack = reverse_a_stack +  a_stack.pop()
    return reverse_a_stack

#iterration
def reverse2(s):
    rs = ""
    for i in range(1,len(s)+1):
        rs = rs + s[len(s)-i]
    return rs

#recursive
def reverse3(s):
    if len(s) == 0:
        return s 
    else:
        return (s[len(s)-1] 
               + reverse3(s[0:len(s)-1]))
  
#swift
def reverse4(s):
    l = list(s)
    temp = ''
    for i in range(0,len(l)//2):
        temp = l[i]
        l[i] = l[len(l)-i-1]
        l[len(s)-i-1]= temp
    return "".join(l) # not str(l), because str(l) will only add two "" to the l

def test(case,l):
    if case == "reverse1":
        for w in words:
            print(reverse1(w)) 
    elif case == "reverse2":
        for w in words:
            print(reverse1(w)) 
    elif case == "reverse3":
        for w in words:
            print(reverse1(w)) 
    elif case == "reverse4":
        for w in words:
            print(reverse1(w)) 
    else:
        print("which one to test, enter reverse + number(1,2,3,4) please")

words = ["hello","l","follow",""]

test("reverse1",words)
test("reverse2",words)
test("reverse3",words)
test("reverse4",words)