#intcode
#list of integers 1,0,0,3,99
#look at first if 1 , 2, 99
#99 halt
#else error

#1 add next two positions address and store in third

#2 opcode mutliplies
#next opcode> step forward 4

#every 4 split until 99
import itertools
globalans=[]
ran=[]
def makelist(s):
    #convert input into list
    emp=[]
    i=''
    for item in s:
        if item==',':
            emp.append(int(i))
            i=''
        else:
            i=i+item
    emp.append(i)
    return emp
ourlist=(makelist('1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0'))
def paramjust(c,noun,verb):
    
    li=c
    
    li[1]=noun
    li[2]=verb
    return li



def comp(li,inps):
    #computer
    #initial vars
    copy=li
    lists=[]
    count=0
    mode=0
    leng=len(li)-1
    lim=int(len(li)/4)
    item=li
    opcode=0

    while opcode!=99:
        opcode=item[0]
        opcut=str(opcode)
        modes=[]
        if opcode==99:
            return copy
            break

        #detect input modes
        if len(str(opcode))>1 and (opcut[:-2].count('1') + opcut[:-2].count('0'))==len(str(opcut[:-2])):
            modes=list(opcut[:-2])
            opcode=(opcut[-2:])
        #checking opcodes
        if opcode==1:
            currmode=0
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            if currmode==0:
                val=copy[ind1]+copy[ind2]
                copy[store]=val
            
            item=item[4:]
        if str(opcode)=='01':
            currmode=int(modes.pop()) 
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            if currmode==0:
                v1=copy[ind1]
            elif currmode==1:
                v1=ind1
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                v2=copy[ind2]
            elif currmode==1:
                v2=ind2
            val=v1+v2
            copy[store]=val
            
            item=item[4:]

        
        if opcode==2:
            currmode=0 #del
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            if currmode==0:
                val=((copy[ind1])*(copy[ind2]))
                copy[store]=val
            elif currmode==1:
                val=ind1*ind2
                copy[store]=val
            item=item[4:]
        if str(opcode)=='02':
            currmode=int(modes.pop()) 
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            if currmode==0:
                v1=copy[ind1]
            elif currmode==1:
                v1=ind1
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                v2=copy[ind2]
            elif currmode==1:
                v2=ind2
            val=v1*v2
            copy[store]=val
            
            item=item[4:]
        if opcode==3 or str(opcode)=='03':
            addr=item[1]
            #print('func ',inps)
            inp=inps[0]
            copy[addr]=inp
            item=item[2:]
            inps=inps[1:]
            
            
        
            
        if opcode==4:
            
            currmode=0 #del
            addr=item[1]
            if currmode==0:
                print(copy[addr])
                globalans.append(copy[addr])
            item=item[2:]
        if str(opcode)=='04':
            currmode=int(modes.pop())
            addr=item[1]
            if currmode==0:
                print(copy[addr])
                globalans(copy[addr])
            elif currmode==1:
                print(addr)
                globalans(addr)
            item=item[2:]
        if opcode==5:
            f=item[1]
            s=item[2]
            if copy[f]!=0:
                pos=copy[s]
                item=copy[pos:]
            else:
                pos=3
                item=item[pos:]
        if str(opcode)=='05':
            currmode=int(modes.pop())
            f=item[1]
            s=item[2]
            if currmode==0:
                val1=copy[f]
            elif currmode==1:
                val1=f
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                val2=copy[s]
            elif currmode==1:
                val2=s
            if val1!=0:
                pos=val2
                item=copy[pos:]
                
            else:
                pos=3
                item=item[pos:]
        if opcode==6:
            f=item[1]
            s=item[2]
            if copy[f]==0:
                pos=copy[s]
                item=copy[pos:]
            else:
                pos=3
                item=item[pos:]
        if str(opcode)=='06':
            currmode=int(modes.pop())
            f=item[1]
            s=item[2]
            if currmode==0:
                val1=copy[f]
            elif currmode==1:
                val1=f
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                val2=copy[s]
            elif currmode==1:
                val2=s
            if val1==0:
                pos=val2
                item=copy[pos:]
            else:
                pos=3
                item=item[pos:]
        

        if opcode==7:
            fi=item[1]
            se=item[2]
            ind=item[3]
            if copy[fi] <copy[se]:
                copy[ind]=1
            else:
                copy[ind]=0
            item=item[4:]
        if str(opcode)=='07':
            currmode=int(modes.pop())
            fi=item[1]
            se=item[2]
            ind=item[3]
            if currmode==0:
                val1=copy[fi]
            elif currmode==1:
                val1=fi
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                val2=copy[se]
            elif currmode==1:
                val2=se
            if val1 <val2:
                copy[ind]=1
            else:
                copy[ind]=0
            item=item[4:]
        if opcode==8:
            fi=item[1]
            se=item[2]
            ind=item[3]
            if copy[fi] ==copy[se]:
                copy[ind]=1
            else:
                copy[ind]=0
            item=item[4:]
        if str(opcode)=='08':
            currmode=int(modes.pop())
            fi=item[1]
            se=item[2]
            ind=item[3]
            if currmode==0:
                val1=copy[fi]
            elif currmode==1:
                val1=fi
            if modes==[]:
                currmode=0
            else:
                currmode=int(modes.pop())
            if currmode==0:
                val2=copy[se]
            elif currmode==1:
                val2=se
            if val1 ==val2:
                copy[ind]=1
            else:
                copy[ind]=0
            item=item[4:]
        if opcode==99:
            return copy
            break
        
        #elif opcode not in [1,2,3,4,99,'04','03','02','01','08','07','06']:
            #print()
        item = copy[((len(item)*(-1))):]
    
    return globalans




def amps(newinp,data):
    copier=newinp
    signal=0         
    nip=[newinp[0],signal]
    newinp=newinp[1:]
    cutoff=data.index(99)+1
    #print(nip)
    #for amplifer in range(0,5):
    amplifer=0
    while amplifer!=5:
        amplifer=amplifer+1
        print('nip',nip)
        a=comp(data,nip)
        #print(a)
        nip=[]
        #print(newinp)
        #print(amplifer)
        
        outp=globalans.pop()
        print('outp',outp)
        ran.append(nip)
        
        #newinp=newinp[1:]
        
        if amplifer==5:
            #nip.append(outp)
            newinp=copier
            nip=[]
            nip.append(newinp[0])
            nip.append(outp)
            #amplifer=0
        
        else:
            nip.append(newinp[0])
            nip.append(outp)
            #print('n',nip)
        newinp=newinp[1:]

        #print(a)      

    print("new")
    return(outp)
def combinator(store):
    #list called store
    lioli=[]
    lioli.append(list(itertools.permutations(store)))
    
    return(lioli)


#amps([4,3,2,1,0],[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0])
#amps([0,1,2,3,4],[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0])
#biglist=combinator([5,6,7,8,9])
biglist=combinator([0,1,2,3,4])
massivelist=[]
for thing in biglist[0]:
    li=list(thing)
    #print(li)
    #first test case
    #massivelist.append(amps(li,[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]))

    #second test case
    '''massivelist.append(amps(li,[3,23,3,24,1002,24,10,24,1002,23,-1,23,
101,5,23,23,1,24,23,23,4,23,99,0,0]))'''
    #third test case
    
    '''massivelist.append(amps(li,[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]))'''
    #puzzle
    massivelist.append(amps(li,[3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]))
    #print(massivelist)
    #one
    #massivelist.append(amps(li,[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
#27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]))
maxim=(max(massivelist))
print(maxim)
ind1=massivelist.index(maxim)
print(biglist[0][ind1])

