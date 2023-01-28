def long(strs):
   if len(strs)==0:
       return ""
   minle = len(strs[0])
   for i in range(len(strs)):
       minle=min(minle,len(strs[i]))

   lcp=""
   i=0
   while i<=minle:
       char=strs[0][i]
       for j in range (1,len(strs)):
           if strs[j][i]!=char:
               return lcp
       lcp=lcp+char
       i=i+1
   return lcp

strs=["flower","flow","fly"]
final=long(strs)
print(final)

