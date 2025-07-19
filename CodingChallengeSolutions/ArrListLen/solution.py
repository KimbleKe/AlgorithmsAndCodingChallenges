# author: Kimble Ke
# date: 2025.7.2
 
# O(N) solution
def solution1(A):
  i=0
  count=0
 
  while count<len(A):
    count+=1
    if A[i]!=-1:
      i=A[i]
    else:
      break
 
  return count
