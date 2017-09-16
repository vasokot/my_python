##выводит N-размерную спираль увеличивающихся чисел

n = int(input())

b=[[0 for i in range(n)] for j in range(n)]

z=0
bi=0
bj=1
ei=n
ej=n



i=0
j=0

istep =1
jstep =1

fin=False

while not fin:
  
  if ei-bi == 0 and ej-bj == 0 :
    break
    
  for i in range(bi,ei,istep):
    z +=1        
    b[j][i]=z
  
  if bi<ei:
    bi1=bi
    bi =i-1
    ei = bi1-1
    istep =-1
  else:
    bi1=bi
    bi =i+1
    ei =bi1+1
    istep =1
 
  if ei-bi == 0 and ej-bj == 0 :
     break
     
 
  for j in range(bj,ej,jstep):
    
    b[j][i]=z+1
    z+=1
    
  if bj<ej:
    bj1=bj
    bj =j-1
    ej = bj1-1
    jstep =-1
  else:
    bj1=bj
    bj =j+1
    ej =bj1+1
    jstep =1    



for k in range(len(b)):
  for d in range(len(b[k])):
      print(b[k][d], end=' ')
  print()