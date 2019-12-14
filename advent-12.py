#moon energy

class moon():
    def __init__(self,pos):
        self.pos=pos
        self.velocity=[0,0,0]
        self.potential=0
        self.kinetic=0
        self.total=0
        self.previousvel=[]
        self.previouspos=[]

    def getvel(self):
        v= self.velocity
        return v
    def getpos(self):
        p= self.pos
        return p


def getinput(filename):
    f=open(filename,'r')
    outlist=[]
    output=[]
    for line in f:
        for x in line:
            if x in ['<','x','=','y','z','>','\n',',']:
                #print(x)
                line=line.replace(x,'')
        outlist.append(line)
    #print(outlist)
    for item in outlist:
        output.append(list(item.split(" ")))
    return (output)


def applygravity(moon1,moon2):
    if moon1.pos[0]> moon2.pos[0]:
        moon1.velocity[0]=moon1.velocity[0]-1
        moon2.velocity[0]=moon2.velocity[0]+1
    if moon2.pos[0]> moon1.pos[0]:
        moon2.velocity[0]=moon2.velocity[0]-1
        moon1.velocity[0]=moon1.velocity[0]+1
    if moon1.pos[1]> moon2.pos[1]:
        moon1.velocity[1]=moon1.velocity[1]-1
        moon2.velocity[1]=moon2.velocity[1]+1
    if moon2.pos[1]> moon1.pos[1]:
        moon2.velocity[1]=moon2.velocity[1]-1
        moon1.velocity[1]=moon1.velocity[1]+1
    if moon2.pos[2]> moon1.pos[2]:
        moon2.velocity[2]=moon2.velocity[2]-1
        moon1.velocity[2]=moon1.velocity[2]+1
    if moon1.pos[2]> moon2.pos[2]:
        moon1.velocity[2]=moon1.velocity[2]-1
        moon2.velocity[2]=moon2.velocity[2]+1
    #print(moon1.pos,' ',moon1.velocity)
    #print(moon2.pos,' ',moon2.velocity)
    
def applyvelocity(moon1):
    moon1.pos[0]=moon1.pos[0]+moon1.velocity[0]
    moon1.pos[1]=moon1.pos[1]+moon1.velocity[1]
    moon1.pos[2]=moon1.pos[2]+moon1.velocity[2]
    
    #print(moon1.pos,' ',moon1.velocity)
    
def display(moon1,moon2,moon3,moon4):
    print(moon1.pos,' ',moon1.velocity)
    print(moon2.pos,' ',moon2.velocity)
    print(moon3.pos,' ',moon3.velocity)
    print(moon4.pos,' ',moon4.velocity)
    
def applygravall(moon1,moon2,moon3,moon4,megapos,ind):
    applygravity(moon1,moon2)
    applygravity(moon3,moon4)
    applygravity(moon3,moon2)
    applygravity(moon4,moon1)
    applygravity(moon1,moon3)
    applygravity(moon2,moon4)
    

def applyvelall(moon1,moon2,moon3,moon4,mega,ind):
    applyvelocity(moon1)
    applyvelocity(moon2)
    applyvelocity(moon3)
    applyvelocity(moon4)
    

   
def moonenergy(moon1):
    #potential multiplued by kinetic
    potential=0
    for i in moon1.pos:
        if i<0:
            i=i*(-1)
        potential=potential+i
    #print('potential: ',potential)
    kinet=0
    for t in moon1.velocity:
        if t<0:
            t=t*(-1)
        kinet=kinet+t
    #print('kinetic: ',kinet)
    moon1.potential=potential
    moon1.kinetic=kinet
    moon1.total=kinet*potential
    #print('total: ')
    #print(moon1.total)

def allenergy(li,moon1,moon2,moon3,moon4):
    moonenergy(moon1)
    moonenergy(moon2)
    moonenergy(moon3)
    moonenergy(moon4)
    tot=(moon1.total)+(moon2.total)+(moon3.total)+(moon4.total)
    print('sum of total energy: ',tot)

def check(moon1,moon2,moon3,moon4,li,li2,li3,li4,pos1,pos2,pos3,pos4):
    #li[#instance[#vel[]]]
    #li2[#instance[#pos[]]]
    outt=False
    outt2=False
    #print('curr: ',moon1.velocity)
    #print('prev: ',li)
    if moon1.velocity in li:
        ind1=li.index(moon1.velocity)
        if moon2.velocity == li2[ind1]:
            if moon3.velocity == li3[ind1]:
                if moon4.velocity == li4[ind1]:
                    #print(li)
                    #print(moon1.velocity)
                    outt=True
    if moon1.pos in pos1:
        ind2=pos1.index(moon1.pos)
        if moon2.pos == pos2[ind2]:
            if moon3.pos == pos3[ind2]:
                if moon4.pos == pos4[ind2]:
                    outt2=True
   
    return outt and outt2
    

lioli=getinput('day12.txt')
#print(lioli)
for lis in lioli:
    for i in range(0,len(lis)):
        #print(lis[i])
        lis[i]=int(lis[i])
#print(lioli)
IO=moon(lioli[0])
Europa=moon(lioli[1])
Ganymede=moon(lioli[2])
Callisto=moon(lioli[3])
IOposes=[]
Europoses=[]
ganyposes=[]
callistoposes=[]
IOvels=[]
Europavels=[]
ganyvels=[]
callistovels=[]
print('step 0')
display(IO,Europa,Ganymede,Callisto)
steps=1000
IOposes.append(IO.getpos())
epos=Europa.getpos()
Europoses.append(epos)
gpos=Ganymede.getpos()
ganyposes.append(gpos)
cpos=Callisto.getpos()
callistoposes.append(cpos)
iovel=IO.getvel()
IOvels.append(iovel)
evel=Europa.getvel()
Europavels.append(evel)
gvel=Ganymede.getvel()
ganyvels.append(gvel)
cvel=Callisto.getvel()
callistovels.append(cvel)

for i in range(1,steps+1):
    print('step :',i)
    
    #mega.append([[],[],[],[]])
    #megapos.append([[],[],[],[]])
    applygravall(IO,Europa,Ganymede,Callisto,[],i)
    
    
    applyvelall(IO,Europa,Ganymede,Callisto,[],i)
    
    display(IO,Europa,Ganymede,Callisto)
    if check(IO,Europa,Ganymede,Callisto,IOvels,Europavels,ganyvels,callistovels,IOposes,Europoses,ganyposes,callistoposes)==True:
        
        print('HERE: ','sTEP: ',i)
    print('display')
    display(IO,Europa,Ganymede,Callisto)
    IOposes.append(IO.getpos())
    epos=Europa.getpos()
    Europoses.append(epos)
    gpos=Ganymede.getpos()
    ganyposes.append(gpos)
    cpos=Callisto.getpos()
    callistoposes.append(cpos)
    iovel=IO.getvel()
    IOvels.append(iovel)
    evel=Europa.getvel()
    Europavels.append(evel)
    gvel=Ganymede.getvel()
    ganyvels.append(gvel)
    cvel=Callisto.getvel()
    callistovels.append(cvel)
    allenergy([],IO,Europa,Ganymede,Callisto)
