n=int(input("enter the digit"))
i=n
rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10
if i==rev:
    print("number is palindrome")
else:
    print("number is not a palindrome")
