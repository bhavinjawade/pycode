arr=map(int,input().split())
d=int(input())
arr=arr[d:]+arr[:d]
print(arr)
