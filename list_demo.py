x = 2 # cpu willallocate 4 bytes in memory, give the name x to that, value is 2

data = [1,2,3, 4, 5]

week = ['sun','mon','tue','wed','thu','fri','sat']

for item in data:
    square = item**2
    print(item,square)

l = len(week)
print(l)

for day in week: # change to work with range
    print(day)

for i in range(len(week)):
    print(week[i],end='\t')
