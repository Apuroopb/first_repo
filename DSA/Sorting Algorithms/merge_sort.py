#Time Complexity : O(nlogn)
#Space Complexity: O(n)
def mergesort(l):
    if(len(l)==1):
        return l
    mid = len(l)//2
    left_array = l[0:mid]
    right_array = l[mid:len(l)]
    left_array = mergesort(left_array)
    right_array = mergesort(right_array)
    l = merge(left_array,right_array)
    return l
def merge(l1,l2):
    sorted_array=[]
    while(len(l1)>0 and len(l2)>0):
        if(l1[0]>l2[0]):
            sorted_array.append(l2[0])
            l2.pop(0)
        else:
            sorted_array.append(l1[0])
            l1.pop(0)
    if(len(l1)>0):
        [sorted_array.append(i) for i in l1]
    if(len(l2)>0):
        [sorted_array.append(i) for i in l2]
    return sorted_array

l=[3,5,2,1,4,6,7,9,4]
c=mergesort(l)
print(c)