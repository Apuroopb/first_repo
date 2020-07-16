#Time Complexity: O(n^2)
#Space Complexity: O(1)
def bubble_sort(l):
  for i in range(0,len(l)):
    swapped = False
    for j in range(0,len(l)-i-1):
      if(l[j] > l[j+1]):
        l[j],l[j+1] = l[j+1],l[j]
        swapped = True
    if(swapped == False):
      return l
  return l

