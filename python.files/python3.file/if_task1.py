#WAP to check a 3-digit number is palindrome or not
#n=123:rev_n=321
 
n=int(input("Enter a numer to check palindrome\n"))

d1=n//100
d2=n%10

if d1==d2:
 print("Number is palindeome")
 
if d1!=d2:
 print("Number is not palindome")