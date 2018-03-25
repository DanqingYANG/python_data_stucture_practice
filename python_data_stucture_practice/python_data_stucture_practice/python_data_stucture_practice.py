pairs = 0
class person():
    def __init__(self, num):
        self.id = num
        self.done = False

def print_persons(persons):
    row = []
    for p in persons:
        row.append(p.id)
    print(row)

def is_couple(i,j,persons):
    if not i%2 == 0: # (i+(i+1))%4 == 1 
        return False
    elif (persons[j].id - persons[i].id == 1 and persons[i].id%2 == 0) or (persons[j].id - persons[i].id == -1 and persons[j].id%2 == 0):
        return True
    else:
        return False

def check_who_is_done(persons, pairs):
    for i in range(0,len(persons),2):
        if persons[i+1].id - persons[i].id > 1 or  persons[i+1].id - persons[i].id < -1:
            continue
        elif is_couple(i,i+1,persons):
            persons[i].done   = True
            persons[i+1].done = True
            pairs = pairs + 1
        else:
            continue
    return pairs

def swap(i,j,alist):
    print (str(alist[i].id) +" <> "+ str(alist[j].id))
    temp = alist[i]
    alist[i] = alist[j]
    alist[j] = temp
    print_persons(alist)
    
   
def exchange(persons, pair):
    min_swap = 0
    find_two_couples = False
    for i in range(len(persons)-1):
        if persons[i].done == False:
            for j in range(i+1,len(persons)-1):
                if persons[j].done == True:
                    continue
                #if find one couple
                if is_couple(i,j,persons):
                    #if two couples can be found
                    if is_couple(i+1,j-1,persons):
                        find_two_couples = True
                        swap(i,j,persons)
                        min_swap = min_swap + 1
                        pair = pair + 2
                        for n in [i,i+1,j,j-1]:
                            persons[n].done = True
                    elif is_couple(i+1,j+1,persons):
                        find_two_couples = True
                        swap(i,j,persons)
                        min_swap = min_swap + 1
                        pair = pair + 2
                        for n in [i,i+1,j,j+1]:
                            persons[n].done = True

    if find_two_couples == False:
        for i in range(len(persons)-1):
            if persons[i].done == False:
                for j in range(i+1,len(persons)-1):
                    if persons[j].done ==True:
                        continue
                    if is_couple(i,j,persons):
                        swap(i+1,j,persons)
                        min_swap = min_swap + 1
                        pair = pair + 1
                        for n in [i,i+1]:
                            persons[n].done = True
    return min_swap

row =[]
for i in range(0,10):
    row.append(i)
from random import shuffle
shuffle(row)
#row = [4,0,1,2,3,5,6,7]
print(row)

persons = []
for i in range(len(row)):
    persons.append(person(row[i]))

pairs = check_who_is_done(persons,pairs)
min_swap = exchange(persons,pairs)

print_persons(persons)
