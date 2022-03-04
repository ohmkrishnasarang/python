import filecmp

s=filecmp.cmp("saru.txt",'saru_cpy.txt')
print(s)
