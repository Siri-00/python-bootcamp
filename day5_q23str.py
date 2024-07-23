# input->hello123
# output->6
check="0123456789"
s=input()
c=0
for i in s:
    if i in check:
        c+=int(i)
print(c)