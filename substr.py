def maxlen(str):
    n=len(str)
    if n<2:
        return n
    
    len1=set(str)  
    len2=len(len1)
    
    count1=n+1
 
    a={}
    start=0; c=1
    a[str[start]]=1
    while c<n:
 
        if str[c] in a: a[str[c]]+=1
 
        else: a[str[c]]=1
 
        if len(a)==len2:
 
            while start<c and a[str[start]]>1:
                a[str[start]]-=1
                start+=1
            if count1>c+1-start: count1=c+1-start
        c+=1
 
    print(count1)
 
    
enterstring=str(input())
maxlen(enterstring)
