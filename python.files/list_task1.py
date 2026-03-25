''' WAP to create list containing 10 elements of list where

* odd index element must be printed
* even index element sum must be calculate'''

l=[10,20,30,40,50,60,60,70,80,90,100]

print("odd index elements:")
s=0

for i in range (len(l)):
    if i%2==0:
        s+l[i]
    else :
     print(l[i])
     
print("Sum of even index elements ",s)