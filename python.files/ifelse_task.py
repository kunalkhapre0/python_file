#WAP to check a 3-digit number is armstrong or not 
#n=123 : 1^3  +  2^3  +  3^3  : 1+8+27  :  36

n=int(input("Enter a number to check armstrong\n*"))

d1=n//1000
d2=(n//10)%10
d3=n%10

new_n=d1**3+d2**3**d3**3

if n==new_n:
    print("Number is armstrong")
    
else :
    print ("Number is not armstrong")