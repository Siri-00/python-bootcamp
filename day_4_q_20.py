#leap year
year=int(input())
year1=int(input())
count=0
for i in range(year,year1+1):
    if i%400==0:
        print(i,"is leap year")
    elif(i%4==0 and i%100!=0):
        print(i,"is leap year")
        count+=1
    else:
        print("not a leap year")
print(count)