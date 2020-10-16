def insertion_sort(a,start,end):
	n=len(a)

	for i in range(start+1,end+1):
		key=a[i]
		j=i-1
		while j>=start and a[j]>key: 
			a[j+1]=a[j]
			j-=1
		a[j+1]=key
	return a


def merge(a,start,mid,end):
	if mid==end:
		return a
	l = a[start:mid+1]
	r = a[mid+1:end+1]
	i=0
	j=0
	arr=[]
	while i<len(l) and j<len(r):
		if l[i]<r[j]:
			a.append(l[i])
			i+=1
		else:
			a.append(r[j])
			j+=1

	while i<len(l):
		a.append(l[i])
		i+=1
	while j<len(r):
		a.append(r[j])
		j+=1
	return a


def timsort(a):
	n=len(a)
	min_run=32				#Choosing minimum size to be sorted at one point
	for i in range(0,n,min_run):
		insertion_sort(a,i,min(n-1,(i+min_run-1)))

	size=min_run
	while(size<n):
		for start in range(0,n,size*2):
			mid=(start+size-1)
			end=min(n-1,(start+size*2-1))
			a=merge(a,start,mid,end)		#Two arrays of size = min_run will be merged
		size *=2							
	print("Elements After Sorting:")
	print(a)

def print_elements(a):
	for ele in a:
		print(ele)


if __name__=='__main__':
	n = int(input('Enter size of array: '))
	a=[]
	for i in range(0,n):
		ele = int(input())
		a.append(ele)

	print("Elements Before Sorting:")
	print_elements(a)
	timsort(a)
