ls=list(input("enter the string: "))
for i in ls:
    
    if i!=" ":
        c=0
        for j in range(0,len(ls)):
            if i==ls[j]:
                c=c+1
                ls[j]=" "
        print(i,"=",c)
