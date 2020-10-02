import math

def create_ST(arr,st,low,high,pos):
  #print(low,high,pos)
  if(low == high):
    st[pos] = arr[low]
    return st
  mid = int((low + high)/2)
  create_ST(arr,st,low,mid,2*pos + 1)
  create_ST(arr,st,mid+1,high,2*pos + 2)
  st[pos] = min(st[2*pos + 1],st[2*pos + 2])
  return st

def next_power_of_2(x):  
    f = 1 if x == 0 else 2**(x - 1).bit_length()
    return f*2 - 1

def query(st,ql,qh,low,high,pos):
  if(ql<=low and qh>=high):
    return st[pos]
  if(ql > high or qh < low):
    return math.inf
  mid = (low + high)/2
  return min(query(st,ql,qh,low,mid,2*pos + 1),
  query(st,ql,qh,mid+1,high,2*pos + 2))

arr = list(map(int,input().split()))
st = [None] * int(next_power_of_2(len(arr)))
sth = create_ST(arr,st,0,len(arr)-1,0)
print("segment tree is " + str(sth))
n,m = input().split()
print("query from range %s to %s is" %(n,m))
print(query(sth,int(n),int(m),0,len(arr)-1,0))
