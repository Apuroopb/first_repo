#Time Complexity: O(logn)
#Space Complexity: O(1)

def binary_search(l,a):
    low,high=0,len(l)-1
    while(high >= low):
        mid = (low + high)//2
        if(l[mid]==a):
            return mid
        elif(l[mid] > a):
            high = mid - 1
        elif(l[mid] < a):
            low = mid + 1
    return -1

def binary_search_recursive(l,start,end,a):
    while(end >= start):
        mid = (start+end)//2
        if(l[mid] == a):
            return mid
        elif(l[mid]>a):
            return binary_search_recursive(l,start,mid-1,a)
        elif(l[mid]<a):
            return binary_search_recursive(l,mid+1,end,a)
    return -1
l = [1,2,3,4,5,6,7,8]
l.sort()
print(l)
val = -1
print("search for value:",binary_search(l,val))
print("search for value:",val,binary_search_recursive(l,0,len(l)-1,val))

