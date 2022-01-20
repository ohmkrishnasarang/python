a=int(input("enter the value:"))
def neon(x):
    sqr=(x**2)
    temp=x
    sum=l=0
    while(temp>0):
         l=temp%10
         sum=sum+l
         temp=temp//10
    if sum==x:
        print(x,"is a neon")
    else:
        print(x,"is not neon")
neon(a)
        
   
