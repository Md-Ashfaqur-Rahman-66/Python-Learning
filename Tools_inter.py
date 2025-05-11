## Lists

# mylist = ["banana", "5", True, 'banana']    # it supppports char, number, boolian, duplicate
"""print(mylist)"""

"""mylist2 = list()
print(mylist2)"""

"""for x in mylist:             #accessing items from list
    print(x)"""

"""if "banana" in mylist:       #checking items in list 
    print('yes')
else:
    print('no')
if 'lemon' in mylist:
    print('yes')
else:
    print('no')"""

""""print(len(mylist))"""

"""mylist.append("lemon")          # inserting new item at the end
print(mylist)

mylist.insert(1,'blueberry')        #inserting new item at specific index position
print(mylist)"""

"""item = mylist.pop()              # remove last item
print(item)                         # give the last removed item
print (mylist)

mylist.remove(True)                 # remove specific item
print(mylist)

print(mylist.clear())"""

# mylist = [4, 3,38, 1, 32]

"""mylist.sort()                    # sort the actual list
print(mylist)

newlist = sorted(mylist)            # doesn't sort the actual list
print(newlist)
print(mylist)"""

"""mylist = [0] * 5                    # same elements multiple times
print(mylist)

print([2,2,4,4]+ mylist)"""            # linear property

"""mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5]                         # assigining upto 4th index position
a = mylist[1:]  
a = mylist[:5]
a = mylist[1::1]
a = mylist[1::2]                        # taking the 2nd items
a = mylist[::-1]                        # inversing the list
print(a)"""

"""list_org = ['banana', 'cherru', 'apple']
#list_cpy = list_org                     # making th eorg and cpy list same
#list_cpy = list_org[:]                   #slicing
#list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy.append("lemon")
print(list_cpy)
print(list_org)"""

"""a = [1,2,3,4,5,6]
b = [i*i for i in a]                    # making a list from previous list
print(a)
print(b)"""

# Tuples (similar to list but can't be changed after created)

""""#mytuple = ('Max', 28, 'Boston')
mytuple = 'Max', 28, 'Boston'
print(mytuple)
mytuple = ('Max')
print(type(mytuple))
mytuple = ('Max',)
print(type(mytuple))"""

"""mytuple = tuple(['Max', 28, 'Boston'])
print(mytuple)

item = mytuple[2]
print(item)

# mytuple[0] = "Tim"              # can't made any change according to definintion

for i in mytuple:
    print(i)

if 'Max' in mytuple:
    print("yes")
else:
    print("Not")"""

"""my_tuple = ('a','b','c','e','j','a')

print(my_tuple.count('a'))
print(my_tuple.index('a'))

my_list = list(my_tuple)            # converting tuple > list
print(type(my_list))

my_tuple2 = tuple(my_list)          # converting list > tuple
print(type(my_tuple2))"""

"""a = [1,2,3,4,5,6,7,8,9,10]
b = a[2:5]
c = a[:5]
d = a[::2]
e = a[::-1]
print(b, c, d, e)"""

"""my_tuple = 'Luban', 23, 'Dhaka'
name, age, city = my_tuple          # Unpacking og tuple
print(name)
print(age)
print(city)"""

"""my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple              # i2 is a list with middle elements
print(i1)
print(i3)
print(i2)
print(type(i2))"""

"""import sys                           # Tuple is more efficient then list
my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), 'bytes')
print(sys.getsizeof(my_tuple), 'bytes')

import timeit
print(timeit.timeit(stmt = "[0,1,2,3,4,5]", number = 100000))
print(timeit.timeit(stmt = "(0,1,2,3,4,5)", number = 100000))"""

# Dictionaries: key-Value pairs, Unordered, Mutable

"""mydict = {'name': 'luban', 'age': 23, 'city': 'Dhaka'}
print(mydict)

mydict2 = dict(name='Atiar', age=18, city='Dhaka')          # name/age/city: key, mary/28/Boston: value
print(mydict2)

print(mydict2['name'], mydict['name'])                      # accessing items form dictionary

mydict['email']='arluban@gmail.com'                         # adding new key-value
mydict2['email']='aremon@gmail.com'
print(mydict, mydict2)

del mydict['age']                                           # deleting a kew-item
print(mydict)
mydict2.pop('age')
print(mydict2)

if 'lastname' in mydict:            # checking if key-value is present
    print(mydict['lastname'])
else:
    print(mydict['name'])

try:
    print(mydict2['lastname'])
except:
    print('not present')

for key in mydict:                  # using loop to excess key-items
    print(key)
for key,value in mydict.items():
    print(key, value)

mydict_cpy = mydict         # dedicate mydict_cpy and mydict to same memory location
mydict_cpy['nmbr'] = 1234
print(mydict_cpy)
print(mydict)

mydict_cpy = mydict.copy()      # dedicate mydict_cpy and mydict to different memory location
mydict_cpy['married'] = 'no'
print(mydict_cpy)
print(mydict)"""

"""mydict = dict(name= 'luban', age= 23, city= 'Dhaka')
mydict2 = dict(name='Atiar', age=18, city='Dhaka', email='aremon@gmail.com')

mydict.update(mydict2)
print(mydict)

#mydict3 = dict(name='luban', 2==4, 4==16, 5==25)      # numbers can't be use as key in this way

mydict3 = {2:4, 4:16, 6:16}         # numbers can be used as key in this way
print(mydict3)

mytuple=(3,5)               # tuple can be used as key but not list
mydict3 = {mytuple: 8}     
print(mydict3)"""

# Sets: unordered, mutable, no duplicates
# ()= Tuple, {}= Dictionary(2 elements-key)/Sets(single values), []= List

"""set1={1,2,3,4,3,1}          # no duplicated
print(set1)

set2=set([1,2,3,4,3,2,1])   # set fucntion for list
print(set2)

set3=set('Hello')           # unordered
print(set3)

set4 = {}           # Emty Dictionary
set5 = set()        # Emty Set
print(type(set4))
print(type(set5))"""

"""set6= set([11,22,33,44,55])
set6.add(1)         # adding element
set6.add(2)
set6.add(3)
set6.add(4)
set6.remove(3)      # removing element
set6.discard(2)     # same
print(set6.pop())   # arbitrarily move pick element and remove it
print(set6)

for i in set6:
    print(i)

if 1 in set6:
    print('yes')"""

"""odds = {1,3,5,7,9}
evens = {2,4,6,8}
primes = {2,3,5,7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
I = i = odds.intersection(primes)
print(i)"""

"""setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff1 = setA.difference(setB)               # setA-setB
diff2 = setA.symmetric_difference(setB)     # (setA-setB) U (setB-setA)
print(diff1, diff2)
setA.update(setB)
print(setA)
setB.intersection_update(setA)          # setB = setA intersection setB
print(setB)
setA.difference_update(setB)            # setA = setA-setB
print(setA)
setA.symmetric_difference_update(setB)  # setA = (setA-setB) U (setB-setA)
print(setA)"""

"""setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8,9}
print(setB.issubset(setA), setA.issubset(setB), setA.issuperset(setB), setB.issuperset(setA), setA.isdisjoint(setC))

setD = setC.copy()
setE = set(setB)
print(setD, setE)"""

"""a = frozenset([1,2,3,4])
print(a)
a.remove(2)                 # Error: immutable 
print(a)"""

# Strings- Ordered, Immutable, Text representation

"""string1 = 'hello'
string2 = "I'am a programmer"       # for using single quote in a line
string3 = """"""Hello
World""""""                            # for using multiline strings
string4 = """"""Hello \
World""""""                            # for denoting in same line
print(string1, string2)
print(string3, string4)

string5 = "md ashfaqur rahman luban"
char1 = string5[1]                  # accessing char
substring = string5[1:5]            # accessing char from 1 to 5
sub1 = string5[::1]                 # accessing every char
sub2 = string5[::2]                 # accessing every 2nd char
sub3 = string5[::-1]                # reversing the order of the string
print(char1, substring, sub1, sub2, sub3)

greeting = 'Hello'
name = 'Atiar'
sentence = greeting + " " + name    # concatenate two strings
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print('yes')
else:
    print('no')

string6 = '   Hello World   '
print(string6)
print(string6.strip())          # strip the white strings before and after the string

print(string5.upper())
print(string5.lower())
print(string5.startswith('Md'))
print(string5.endswith('Md'))
print(string5.find('L'))
print(string5.find('k'))
print(string5.count('a'))
print(string5.replace('n','p'))

string7 = 'How are you doing'
list = string7.split(" ")       # creating a list from string using space
print(list)
string7 = 'How,are,you,doing'   # creating a list from string using comma
list1 = string7.split(",")
print(list1)
string7 = 'How,are,you,doing'   # creating a list of only 1 element
list = string7.split(" ")
print(list)

string8 = ' '.join(list1)       # Converting list into string
print(string8)

from timeit import default_timer as timer
list2 = ['a'] * 1000000

# Bad way
start = timer()
string9 = ' '
for i in list2:
    string9 += i
stop = timer()
print(stop-start)

# Good way
start = timer()
string10 = ' '.join(list2)
stop = timer()
print(stop-start)

# %, .format(), f-strings
var1 = 'Tom'
string11 = 'the variable is %s' %var1
print(string11)
var2 = 3
string11 = 'the variable is %d' %var2
print(string11)
var3 = 3.1416
string11 = 'the variable is %.3f' %var3
print(string11)

string11 = 'variable1 is {}, variable2 is {}, variable3 is {:.2f}'.format(var1, var2, var3)
print(string11)

string11 = f'variable1 is {var1}, variable2 is {var2*1.5}, variable3 is {var3}'     # Easy and New
print(string11)"""

# Collections (list with tuples is it): Counter, namedtuple, OrderedDict, defaultdict. deque

"""from collections import Counter
a = "aaaaabbbbccc"
counter1 = Counter(a)
print(counter1)
print(counter1.items())
print(counter1.values())
print(counter1.most_common(2))
print(counter1.most_common()[0])
print(counter1.most_common()[0][0])
print(list(counter1.elements()))"""

"""from collections import namedtuple
point = namedtuple('Point', 'x, y')     # Create a class "point" with 2 variables x and y
pt = point(1,-4)                        # assigning the values in those variables
print(pt.x, pt.y)"""

"""from collections import defaultdict
d = defaultdict(int)         # assigning the data type of the variables
e= defaultdict(list)
f= {}
d['a'] = 2
d['b'] = 4
print(d)
print(d['a'])
print(d['c'])                # default value is assignment to 'c'
print(e['a'])               # with a default dict it will create a error"""
# print(f['a'])

"""from collections import deque   # it is Double Ended Que

d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4,5,6])
print(d)
d.extendleft([7,8,9])
print(d)
d.rotate(2)             # rotate the deck 2 digit right
print(d)
d.rotate(-2)            # rotate the deck 2 digit left
print(d)"""

# Itertools: product, permutations, combinations, accumulate, gruopby, and infinite iterators
"""from itertools import product
a = [1,2]
b = [3,4]
c = [5]
prod = product(a,b)
prod1 = product(a,c, repeat=2)
print(list(prod))
print(list(prod1))"""

"""from itertools import permutations
a = [1,2,3]
perm = permutations (a)
perm1 = permutations(a,2)
print(list(perm))
print(list(perm1))"""

"""from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations (a,2)           # no repeatation
print(list(comb))"""

"""from itertools import combinations_with_replacement
a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement (a,2)           # repeatation
print(list(comb_wr))"""

"""from itertools import accumulate
import operator
a = [1, 2,5, 3, 4]
acc = accumulate(a)                     # accumulation by summation
acc1 = accumulate(a, func=operator.mul) # accumulation by multiplications
acc2 = accumulate(a, func=max)          # accumulate maximum
print(a)
print(list(acc))
print(list(acc1))
print(list(acc2))"""

# from itertools import groupby

# Either
"""def smaller_then_3(x):
    return x < 3            # return true or false

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_then_3)
for key, value in group_obj:
    print(key, list(value))"""

# Or
"""a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))"""

"""persons = [{'name': 'Tim', 'age': 25}, {'name':'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj = groupby(persons, key=lambda x: x['age'])
for in group_obj:
    print(key, list(value))"""

from itertools import count, cycle, repeat
"""for i in count(1):
    print(i)
    if i==15:
        break"""

"""a = [1, 2, 3]
b = 0
for i in cycle(a):
    b = b+1
    print(i)
    if b == 4:
        break"""

"""for i in repeat(3, 5):
    print(i)"""























































