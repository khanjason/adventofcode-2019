#go through each num in range
#increment count
#first look for doubles

#savelist
sav=[]

#function which checks maximums of each element
#if next element increases, it is cut
def go(i):

        li=[]
        
        for thing in str(i):
            li.append(int(thing))
        ma=li[0]
        for item in li:
            if item>=ma:
                ma=item
            else:
                li.remove(item)
                
                return
        sav.append(li)

#looks for doubles, if no doubles found the element is cut
#element is also cut if no doubles and only multiples
def doubl(lis):
    rem=[]
    nums=[1,2,3,4,5,6,7,8,9]
    for t in lis:
        c=0
        for x in nums:
            if t.count(x)<2 or t.count(x)>2:
                c=c+1
                if c==9:
                    if t not in rem:
                        rem.append(t)
    for r in rem:
        lis.remove(r)
    return lis






#run function for order in range
    
for i in range(248345,746315):     
    go(i)
#run double checker
print(len(sav))#prints number for first question
print(len(doubl(sav)))#answer to second
