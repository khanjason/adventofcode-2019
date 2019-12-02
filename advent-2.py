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
    copy=li
    lists=[]
    count=0
    lim=int(len(li)/4)
    while count!=lim:
        lists.append(li[:4])
        li=li[4:]
        count=count+1
    
    for item in lists:
        
        if item[0]==1:
            
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            val=copy[ind1]+copy[ind2]
            copy[store]=val
        if item[0]==2:
            ind1=item[1]
            ind2=item[2]
            store=item[3]
            val=((copy[ind1])*(copy[ind2]))
            copy[store]=val
        if item[0]==99:
            
            break
        elif item[0] not in [1,2,99]:
            print("error")
    return copy
            

for i in range(0,99):
    for j in range(0,99):
        # i is noun
        #j is verb
        te=comp([1,i,j,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,99,2,14,0,0])
        
        
        if te[0]==19690720:
            print(i)
            print(j)
            print(100*i+j)
            print('done')
print("new")

