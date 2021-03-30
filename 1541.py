sentence=input().split('-')
result=0

for i in sentence[0].split('+'):
    result+=int(i)
for i in sentence[1:]:
    for j in i.split('+'):
        result-=int(j)
print(result)