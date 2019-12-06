#intcode
#list of integers 1,0,0,3,99
#look at first if 1 , 2, 99
#99 halt
#else error

#1 add next two positions address and store in third

#2 opcode mutliplies
#next opcode> step forward 4

#every 4 split until 99

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



def comp(li):
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

    while len(item)>0:#opcode!=99:
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
            inp=int(input('add input'))
            copy[addr]=inp
            item=item[2:]
            
            
        
            
        if opcode==4:
            
            currmode=0 #del
            addr=item[1]
            if currmode==0:
                print(copy[addr])
            item=item[2:]
        if str(opcode)=='04':
            currmode=int(modes.pop())
            addr=item[1]
            if currmode==0:
                print(copy[addr])
            elif currmode==1:
                print(addr)
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
    
    return copy
            


p=comp([3,225,1,225,6,6,1100,1,238,225,104,0,1102,31,68,225,1001,13,87,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,174,110,224,1001,224,-46,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,13,60,224,101,-73,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,87,72,225,101,47,84,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,76,31,225,1102,60,43,225,1102,45,31,225,1102,63,9,225,2,170,122,224,1001,224,-486,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,29,17,224,101,-493,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,52,54,225,1102,27,15,225,102,26,113,224,1001,224,-1560,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1002,117,81,224,101,-3645,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226])


print(p)      

print("new")

