# find the  element that is present in k+n index
 #input k=3
 #n=2
  #3 6 8 4 61 2
 # output--> 2
 
 #k=3
 #n=4
 # 80 70 54 36 72
#0utput-->error
'''list=list(map(int,input().split()))
k=int(input())
n=int(input())
t=k+n
if (len(list)<k+n):
    print("error")
else:
   for i in range(len(list)):
              print(list[t])
              break'''
   

   #print the element in a particular index
'''list=list(map(int,input().split()))
k=int(input())
for i in range (len(list)):
    print(k%len(list))
          
    break'''

# find the maximum element in a given list
'''list=list(map(int,input().split()))
maxi=list[0]
for i in range(len(list)):
if(list[i]>maxi):
    maxi=list[i]
    print(maxi)'''

# find the minimum element
'''list=list(map(int,input().split()))
min=list[0]
for i in range(len(list)):
 if(list[i]<min):
    min=list[i]
print(min)'''
    
    # replace the element in an array with average of max and min elements
'''list=list(map(int,input().split()))
maxi=list[0]
for i in range(len(list)):
 if(list[i]>maxi):
    maxi=list[i]
    print(maxi)
min=list[0]
for i in range(len(list)):
 if(list[i]<min):
    min=list[i]
print(min)
sum=maxi+min
print(sum)
avg=sum//2
print(avg)
for i in range(len(list)):
    list[i]=avg
print(list)'''

'''#find the missing number in array
list=list(map(int,input().split()))
n=int(input())
m=len(list)
n=n*(n+1)//2
sum=0
for i in range(len(list)):
  sum+=list[i]
print(n-sum)'''


 
# find the duplicates in array
'''list=list(map(int,input().split()))
li=[]
for i in list:
  if(i not in li):
        li.append(i)
print(*li)'''

  # sum of the digits using while loop
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
print(sum)'''
# find the sum of squares of digit in a given number
'''n=123
sum=0
while n>0:
    r=n%10
    sum=sum+r ** 2
    n=n//10
print(sum)'''
# sum of even digits
'''n=int(input())
sum=0
while n>0:
    r=n%10
    if r%2==0:
      sum=sum+r 
    n=n//10
print(sum)'''  

#print reverse of a number -->123-->321
'''n=int(input())
rev=""
while n>0:
   r=n%10
   rev=rev+str(r)
   n=n//10
   ans=int(rev)
   print(ans)
   print(type(ans))'''

#find even or odd
# find greatest of 3
# find peak element in array
# find maximum element in array
# find second maximum in an array
# find second largest element in an array
# reverse an array without using built in functions
# find the sum of squares of given number
#find sum of squares of even or odd
#check whether the given number is palindrome or not using while loop
#write a program to print fibonacci series

#1
'''n=int(input())

if(n%2==0):
    print('even')
else:
   print('odd')'''


#2
'''n1=int(input())
n2=int(input())
n3=int(input())
if (n1>=n2) and (n1>=n3):
    greatest=n1
elif (n2>=n3) and (n2>=n3):
      greatest=n2
else:
     greatest=n3
print("the greatest number is",greatest)'''

#3


'''list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
    if list[i]>list[i-1] and list[i]>list[i+1]:
      print(list[i],end=" ")'''

'''list=list(map(int,input().split()))
count=0
for i in range(1,len(list)-1):
     
   if list[i]>list[i-1] and list[i]>list[i+1]:
           count=i
if(list[-1]>list[-2] and list[-1]>count):
       count=len(list)-1
print(list[count])'''

'''n=25
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''

#4
'''arr=[2,3,4,5,6]
max=arr[0]
for i in range(0,len(arr)):
    if(arr[i]>max):
        max=arr[i]
print(max)'''


#5
'''a=[]
n=int(input())
for i in range(1,n+1):
    b=int(input())
    a.append(b)
a.sort()
print("second largest element is:",a[n-2])'''

#7
'''arr=[1,2,3,4,5]
rev_arr =[]
rev_arr=arr[::-1]
print(rev_arr)'''


# sum of all elements in array
'''n=10
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)'''


#8
'''num=456
a=num%10
num=num//10
b=num%10
c=num//10
add=(a ** 2)+(b ** 2)+(c ** 2)
print(add)'''


#9
'''n=int(input())
i=1
sum=0
while(i<=n):
    sum=sum+(i*i)
    i=i+1
print(sum)'''


#10
'''n=int(input("enter a number"))
pal=n
rev=0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
if(pal==rev):
    print("palindrome number")
else :
    print("not a palindrome number")'''


#11
'''n=int(input())
a=0
b=1
if n==1:
    print(a)
else:
    print(a) 
    print(b)
for i in range(2,n):
 c=a+b
 a=b
 b=c
print(c)'''







    




 
