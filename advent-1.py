#day 1 prt 1

fuelvalues=[]
values=[]
ex=[]
def calc(it):
    it=it/3
    p=int(it)
    p=p-2
    return p
    



f= open("fuelinput.txt",'r')

for x in f:
    x=x[:-1]
    values.append(int(x))
#print(values)
for item in values:
    fuelvalues.append(calc(item))
    #it=int(line)
    #print(it)
    #p=calc(it)
    #fuelvalues=fuelvalues+p
    #print(fuelvalues)

print(fuelvalues)
fu=fuelvalues

for thing in fu:
    t=thing
    while t >0:
        t=calc(t)
        if t>0:
            ex.append(t)
#prin(calc(139349))
print(ex)
print((sum(ex))+(sum(fuelvalues)))
#s=sum(ex)
#print(fuelvalues+s)
f.close()
