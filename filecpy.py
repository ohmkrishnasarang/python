f=open("saru.txt",'r')
s=f.read()
print(s)

f=open("saru_cpy.txt",'w')
f.write(s)
f.close()
