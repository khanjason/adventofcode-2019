
def takeinput(string):
    outlist=[]
    for item in string:
        outlist.append(int(item))
    return outlist

def calcpattern(base,outt,ind,le):
    rlist=[]
    flist=[]
    count=0
    c=0
    #print(le,' ',count)

    while count!=le:
        
        for item in base:
                #print(ind)
                #c=c+1
                #if c==(len(base)-1):
                    #c=0
                for i in range(0,ind):
                    #print(ind)
                    #print(i)
                    rlist.append(item)
                    count=count+1
                    if count==le:
                        return rlist
    return rlist
    



def phase(li,pat):
    totstr=''
    for times in range(0,8):
        #print('next line')
        
        tot=0
        for item in range(0,len(li)):
            c=calcpattern([0,1,0,-1],li,times+1,len(li)+1)
            #print(c)
            offset=c[1:]
            #print(offset)
            #print((li[item]),'*',offset[item])
            tot=tot+(li[item]*offset[item])
        tot=str(tot)
        n=[]
        for thing in tot:
            n.append(thing)
        #print(n[-1])
        t=n[-1]
        totstr=totstr+t
            #print(c[item])
    print('new signal :',totstr)
    return totstr
        
    
    #print(newlist)

def generate(n,base,sig):
    for i in range(0,n):
        print('phase ',i)
        s=phase(sig,base)
        sig=takeinput(s)

#test cases
#mlist=takeinput('12345678')
#mlist=takeinput('80871224585914546619083218645595')
#mlist=takeinput('19617804207202209144916044189917')
#mlist=takeinput('69317163492948606335995924319873')

#puzzle input
mlist=takeinput('59750939545604170490448806904053996019334767199634549908834775721405739596861952646254979483184471162036292390420794027064363954885147560867913605882489622487048479055396272724159301464058399346811328233322326527416513041769256881220146486963575598109803656565965629866620042497176335792972212552985666620566167342140228123108131419565738662203188342087202064894410035696740418174710212851654722274533332525489527010152875822730659946962403568074408253218880547715921491803133272403027533886903982268040703808320401476923037465500423410637688454817997420944672193747192363987753459196311580461975618629750912028908140713295213305315022251918307904937')
        
#print(mlist)
#run generator

generate(100,[0,1,0,-1],mlist)
