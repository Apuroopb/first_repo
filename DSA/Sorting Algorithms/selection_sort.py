#Time Complexity: O(n^2)
#Space Complexity: O(1)
def selection_sort(l):
  for i in range(0,len(l)):
    min = l[i]
    for j in range(i+1,len(l)):
      if(min > l[j]):
        min =l[j]
    if(min < l[i]):
      min,l[i] = l[i],min
  return l 

