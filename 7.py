#you are given with a comma separated natural numbers 1-10 print only even values
'''list=list(map(int,input().split(",")))
for i in range(1,len(list)+1,1):
   if i%2==0:
      print(i)'''
      

    #7.2 how many even numbers are present in above numbers
'''list=list(map(int,input().split(",")))
count=0
for i in range (1,len(list),2):
    count+=1
print(count)'''

#7.3  you are given with a space separated integer list find number of even elements and number of odd elements in a given list
'''list=list(map(int,input().split(" ")))

even=0
odd=0
for i in range (len(list)):
    if i%2==0: 
           even+=1
    else:
       odd+=1
print(even,odd)'''
 
 
  
