ress=''

def get_parent(child):
  r = None
  for key in d:
    if parrent in d[key]:
      r=key
  return r
  

def get_pos(parrent,child):
  ress='No'
  if child in d:
    all_parrents=d[child]
    
  if all_parrents ==[]:
    ress ='No'
  elif parrent in all_parrents:
    ress='Yes'
    
  else:
    for parrent1 in all_parrents:
      if get_pos(parrent,parrent1)=='Yes' :
        ress='Yes'
  
  return ress



d={}
n=int(input())

for i in range(n):
  s=input().split(' : ')
  if len(s)==1 or s[0]==s[1]:
    d[s[0]]=[]
  else:
    if s[0] not in d:
      d[s[0]]=[]
    
    s1=s[1].split()
    for el in s1:
      d[s[0]].append(el)


m=int(input())

for j in range(m):
  s2=input().split()
  res ='No'
  if s2[0] in d and s2[1] in d :
    if (s2[0] == s2[1]):
      res='Yes'
    else:
      res=get_pos(s2[0],s2[1])
  else:
    res='No'
  
  print(res)
  