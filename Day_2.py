#my_list=[1,-2,3,66,876,0]
#my_list.insert(500,6)
#my_list.append(7)
#my_list.pop(4)
#print(my_list)
#print(len(my_list))
#cnt=my_list.count(2)
#print(cnt)
#my_list.sort()
#my_list_2=[5,6,7,8]
#new_lst=my_list_2.copy()
#print(new_lst)
#list as a dynamic-->
'''my_list=list(map(int,input().split(",")))
print("enter your choice\n 1.append\n 2.pop\n 3.sort\n 4.length of list\n")
choice=int(input())
if(choice==1):
   my_list.append(11)
   print(my_list)
elif(choice==2):
   my_list.pop()
   print(my_list)
elif(choice==3):
   my_list.sort()
   print(my_list)
else:
   print(len(my_list))
   print(my_list)'''


#my_list=list(map(int,input(),split(" ")))
# for i in my_list:
# print(i,end=" ")
#s="hello world"
#for i in range(len(s)):
    #print(s[i],end=" ")
    #print()
#for i in s:
    #print(i,end=" ")
#new code
#n=int(input())
#for i in range(1,n):
    #print(i)
#2
#list=[]
#n=int(input())
#for i in range(1,n+1):    
#   list.append(i)
#print(*list)



#3
'''n=int(input())
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''

#my_list=list(map(int,input().split(" ")))
#for i in range(len(my_list)): 
#print(i,end=" ")
#s=input()
#for i in range(len(s)):
  #   print(s[i],end=" ")

#n=input()
#for i in n:
  #  print(i,end=(" "))
  # using for loop 1-100 numbers
  # using for loop 1-100 numbers in empty list
  # find sum of all the numbers in a list

#n=100
#for i in range (n):
 #   print(i)

'''n=int(input())
li=[]
for i in range (1,n+1):
    li.append(i)
print(*li)'''


'''n=100
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''  
  
   


#6
#  takea a space separator input from the user and print alternate elements
#n=100 
#for i in range(0,n,2):
 # print(i)

  # 2.method
'''list=list(map(int,input().split(" ")))
for i in range(0,len(list),2):
    print(list[i])'''

  #  you are given with a comma separator natural numbers 1-10 print only even values


  #7
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
 
 #8
 # 8. givean an space separated integer list find the average of elements present in the even index
'''list=list(map(int,input().split(" ")))
sum=0
count=0
n=len(list)
for i in range(len(list)):
    if(i%2==0):
      sum+=list[i]
      count+=1
print(sum/count)'''
    
#9
#9 write a program to find area of circle
#write a program to find perimeter of circle
# write a program to find area of triangle
#write a program to perimeter of a triangle


#9.3
'''a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)'''

#9.1
'''from math import pi
r=3.00
area=pi*r*r
print("the area of circle is",end=" ")
print(area)'''

#9.4
'''a=int(input())
b=int(input())
c=int(input())
p= a+b+c
print("perimeter\n ",p)'''



#9.2
'''from math import pi
r=35.63
p=2*3.14*r
print(p)'''
    
   
  
   