a=input()
list=[]
for _ in a:
    if _ not in list:
        list.append(_)
print(len(list))
