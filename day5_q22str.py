# check how many vowels are in a astring
str=['a','e','i','o','u']
count=0
inp="hello world"
for i in inp:
    if(i in str):
        count+=1
print(count)

#
check="['a','e','i','o','u']"
i="hello world"
count=0
inp=i.lower()
for i in inp:
    if i in check:
        count+=1
print(count)