answer = []
def index_ceiling(arr,T, left,right, key):
   while (right - left > 1):
      mid = left + (right - left) // 2;
      if (arr[T[mid]] >= key):
         right = mid
      else:
         left = mid
   return right
def long_inc_seq(A):
   n = len(A)
   tails_idx = [0]*(n)
   prev_idx = [-1]*(n)
   length = 1
   for i in range(1, n):
      if (A[i] < A[tails_idx[0]]):
         tails_idx[0] = i
      elif (A[i] > A[tails_idx[length - 1]]):
         prev_idx[i] = tails_idx[length - 1]
         tails_idx[length] = i
         length += 1
      else:
         pos = index_ceiling(A, tails_idx, -1, length - 1, A[i])
         prev_idx[i] = tails_idx[pos - 1]
         tails_idx[pos] = i
   i = tails_idx[length - 1]
   while(i >= 0):
      answer.append(A[i])
      i = prev_idx[i]
def long_bitonic(A,B):
   n1 = len(A)
   n2 = len(B)
   global answer
   long_inc_seq(A)
   answer = answer[::-1]
   B = B[::-1]
   long_inc_seq(B)
A = [2, 6, 3, 5, 4, 6]
B = [9, 7, 5, 8, 4, 3]
long_bitonic(A,B)
print(answer)
