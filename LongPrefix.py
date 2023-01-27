def long(strs):
   minle=strs[0]
   for i in range(len(strs)):
       minle=min(minle,len(strs[i]))
   

strs=["flower","flow","fly"]
out=long(strs)
print(out)

