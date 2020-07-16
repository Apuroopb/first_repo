def insertion_sort(l):
  for i in range(1,len(l)):
    hole = i
    value = l[i]
    while(hole > 0 and l[hole-1] > value):
      l[hole] =l[hole-1]
      hole-=1
    l[hole] = value
  return l