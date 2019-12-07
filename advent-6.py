
#take in input, put in dictionary with second planet: first
lines = list(x.rstrip().split(")") for x in open("day6input.txt"))
orbits = dict(reversed(x) for x in lines)

cnt = 0
#count all orbits in dictionary
for obj in orbits.keys():
  x = obj
  #until COM reached
  while x in orbits:
    x, cnt = orbits[x], cnt + 1
print(cnt)



cnt=0
path=[]
#transverse dictionary from YOU to COM and add to path
for obj in orbits.keys():
  x = obj
  if x == 'YOU':      
      while x !='SAN':
        path.append(x)
        if x=='COM':              
              ind=path.index('COM')
              print(path[ind-1])
              break
        else:    
            x, cnt = orbits[x], cnt + 1
  
print(cnt)
print(path)
cnt=0
path2=[]
#transverse from SAN to COM and add to a path
for obj in orbits.keys():
  x = obj
  if x == 'SAN':
      print(orbits[x])
      
      while True:
        path2.append(x)
        if x=='COM':

              ind=path2.index('COM')

              break
        else:    
            x, cnt = orbits[x], cnt + 1
  
print(cnt)
print(path2)
#find intersect of paths
for thing in path:
    if thing in path2:
        intersect=(thing)
        break
#split paths up to intersect and add
ind1=path.index(intersect)
ind2=path2.index(intersect)
half1=path[1:ind1]
half2=path2[1:ind2]
print(half1)
print(half2)
print('ans:')
print(len(half1)+len(half2))
