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


# takea a space separator input from the user and print alternate elements
#n=100 
#for i in range(0,n,2):
 # print(i)

  # 2.method
list=list(map(int,input().split(" ")))
for i in range(0,len(list),2):
    print(list[i])

  
