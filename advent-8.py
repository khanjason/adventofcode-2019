
#get puzzle input from file
def getpuzzleinput():
    f=open('day8input.txt','r')
    for i in f:
        string=str(i)
    
    arr=string.split()
    newarr=[]
    for t in arr[0]:
        newarr.append(int(t))
    
    return(newarr)

#find where target values are in layer
def highlighter(nlist,target,mlist,index):
    alist=[]
    flayer=mlist[index]
    count=-1
    for row in flayer:
        for item in row:
            count=count+1
            if item==target and count in nlist:
                ind=nlist.index(count)
                alist.append(nlist[ind])
                nlist.remove(count)

    return alist
    

#put in bits in position
def compileimage(total,wlist,blist,fresh):
    output=fresh
    #colours have been switched for clarity
    for i in range(0,total):
        if i in wlist:
            fresh[i]='■'
        if i in blist:
            fresh[i]='□'
    return fresh


#print all layers
def display(megalist):
    count=0
    for i in megalist:
        count=count+1
        for thing in i:
            print(thing)
        print('layer: ',count)

#count zeros
def counting(mli):
    zs=[]
    for layer in mli:
        zcount=0
        for row in layer:
            for item in row:
                if item==0:
                    zcount=zcount+1
                    
        zs.append(zcount)
    return zs

#retrieve a layer based on its number
def getlayerbyindex(mlist,index):
    index=index-1
    for layer in mlist:
        if index==mlist.index(layer):
            return(layer)

#get number of occurrences of target in layer
def getnumbercountoflayer(layer,number):
    count=0
    for row in layer:
        for i in row:
            if i==number:
                count=count+1
    return count

#create layers from data list
def makeformat(wide,tall,data,cut):
    layers=[]
    layer=[]
    for x in range (0,int(cut)):
        for i in range(0,tall):
            layer.append(data[:wide])
            data=data[wide:]
        layers.append(layer)
        layer=[]
    return layers

#get puzzle input into array
data=getpuzzleinput()
cut=((len(data)/25)/6)
#HOW TO CUT LAYERS
mlist=(makeformat(25,6,data,cut))

##PART 1

#get number of zeros
zeros_by_layer=(counting(mlist))
#get minimum
minimum_zeros=min(zeros_by_layer)
mindex=zeros_by_layer.index(minimum_zeros)
#get the layer with minimum zeros
retrieve=getlayerbyindex(mlist,mindex+1)
#get number of 1s in layer
numoones=getnumbercountoflayer(retrieve,1)
#get number of twos in layer
numotwos=getnumbercountoflayer(retrieve,2)

#ANSWER 
#print('answer: ')
#print(numotwos*numoones)

#PART 2
#find limit
print(25*6)
#create position list
numslist=[]
for i in range(0,150):
    numslist.append(i)

#first layer - get white bits
whitelist=highlighter(numslist,1,mlist,0)

#second layer get black bits
blacklist=highlighter(numslist,0,mlist,0)

#go through rest of layers
while numslist!=[]:
    for i in range(1,100):
        whitelist.extend(highlighter(numslist,1,mlist,i))
        blacklist.extend(highlighter(numslist,0,mlist,i))

#create new position list
freshlist=[]
for i in range(0,150):
    freshlist.append(i)
#compile and layer image
image=makeformat(25,6,compileimage(150,whitelist,blacklist,freshlist),cut)

display(image)

