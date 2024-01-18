
#module os
import os
os.getcwd() #get current working directory
wd= "\file\path"
os.chdir(wd) #change working directory

#module sys
import sys
sys.path.append('/package/path') #adds package path to system path

#slicing lists
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:5]     # ['a', 'b', 'c', 'd', 'e']
a[:-1]    # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
a[4:]     # ['e', 'f', 'g', 'h']
a[-3:]    # ['f', 'g', 'h']
a[2:5]    # ['c', 'd', 'e']
a[2:-1]   # ['c', 'd', 'e', 'f', 'g']
a[-3:-1]  # ['f', 'g']



#catch all unpacking
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
car_ages_descending = sorted(car_ages, reverse=True)
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

#striding
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)


#iterators
my_items = ['a', 'b', 'c']
for i, item in enumerate(my_items):
    print(f'{i}: {item}')
    
   
emails = {
'Bob': 'bob@example.com',
'Alice': 'alice@example.com'}

for name, email in emails.items():
    print(f'{name} -> {email}')



#lists comprehensions
[n*n for n in range(1,11) if not n*n % 2]

#set comprehensions
{ x * x for x in range(-9, 10) }

#dictionary comprehensions
{ x: x * x for x in range(5) }


#example of zip in for
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]

longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(f'El nombre mas largo es {longest_name} con longitud de {max_count}')


 
 #functions
def functionName(parameter1, param2,...): 
    function block 
 
#generator function example, yield is the key, they can be used as iterators
def odds(start=1): 
     """return all odd numbers from start upwards"""
     if int(start) % 2 == 0: start = int(start) + 1 
     while True: 
        yield start
        start += 2

#example of use generator function as iterator
 for n in odds(): 
    if n > 7: break
    else: print(n)
    

#example of lambda function
straight_line = lambda m,x,c: m*x+c
straight_line(2,4,-3)


