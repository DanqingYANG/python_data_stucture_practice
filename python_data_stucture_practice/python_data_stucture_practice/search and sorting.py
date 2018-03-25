'''
mergesort not completed
search: 
    'in'
    binary search
sort: 
    quick:
        1. exchange left with right according to the pivot value, return the split point
        2. recursive, to/from the split point ...-1/+1..., left and right partitions
    merge:
        
    shell:

    insertion:
       get the next and put it in order

    selection: 
       find the lagest then replace
       1.find the lagest: compare -> compare -> ... -> compare O(n^2)
       2.replace the lagest with the current end 
         n(n-1)/2
    bubble: 
       continue compare and exchange
       1. compare and if lager exchange it with the next:
          (compare -> exchange) -> (compare -> exchange) ->...->(compare -> exchange)
         n(n-1)/2
'''

#binary search
def binary_search(n, l):
    if len(l) == 0:
        return False
    else:
        mid = len(l)//2
        if n == l[mid]:
            return True
        elif n < l[mid]:
            return binary_search(n, l[0:mid])
        else:
            return binary_search(n, l[mid+1:len(l)-1])

def bubble_sort(alist):
    for i in range(0,len(alist)-1):
        for j in range(0,len(alist)-i-1):
            temp = alist[0]
            if alist[j] > alist[j+1]:
                swap(alist,j,j+1)
    return alist
 
def selection_sort(alist):
    # too simple
    return alist

#recursive
def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1, last)

def partition(alist,first,last):
    leftmark = first +1
    rightmark = last
    done = False
    while not done:
        while alist[leftmark] <= alist[0] and leftmark < rightmark:
            leftmark = leftmark + 1
        while alist[rightmark] >= alist[0] and rightmark > leftmark:
            rightmark = rightmark - 1
        if rightmark > leftmark: # interfered case shows up
            done = True
        else:
            #exchange values
            swap(alist,leftmark,rightmark)
            '''
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp  
           '''

    #this part is the most complicated part
    #move the alist[first], which should be the biggest in alist[ first : rightmark]
    #exchange the value of alist[first] and alist[rightmark]

    return rightmark

def swap(alist,index_1,index_2):
    temp = alist[index_1]
    l[index_1] = l[index_2]
    l[index_2] = temp
    return

def quick_sort(alist):
    quick_sort_helper(alist,0,len(alist)-1)

def merge_sort(alist):
    e
    return alist

# in
l = [7,9,2,10,1,8,3,4,5,6]
l.pop
print(2 in l)
print(7 in l)

def test(l):
    quick_sort(l)
    bubble_sort(l)
    selection_sort(l)
    print(binary_search(2, l))
    print(binary_search(7, l))

test(l)