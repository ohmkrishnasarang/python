a=int(input("enter the value of A:"))
b=int(input("enter the value of B:"))
def calc(x,y):
    s=x+y
    d=x-y
    p=x*y
    div=x/y
    return(s,d,p,div)
l=calc(a,b)
print("sum=",l[0])
print("difference=",l[1])
print("product=",l[2])
print("division=",l[3])
