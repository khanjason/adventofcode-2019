#day 1 

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

for item in values:
    fuelvalues.append(calc(item))
    

print(fuelvalues)
fu=fuelvalues

for thing in fu:
    t=thing
    while t >0:
        t=calc(t)
        if t>0:
            ex.append(t)
#fuelvalues store module mass costs
#ex store fuel costs
print(ex)
print((sum(ex))+(sum(fuelvalues)))

f.close()
