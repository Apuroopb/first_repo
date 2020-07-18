#Time Complexity : O(n^2)
#Space Complexity: O(1)
def partition(arr,left,right):
    pivot = arr[right]
    i = left -1
    for j in range(left, right):
        if(arr[j] < pivot):
            i+=1
            arr[j],arr[i] = arr[i], arr[j]
    arr[i+1],arr[right] = arr[right],arr[i+1]
    return i+1

def quick_sort(arr,left,right):
    if(left < right):
        pi = partition(arr,left,right)
        quick_sort(arr,left,pi-1)
        quick_sort(arr,pi+1,right)
    return arr
arr=[1,3,2,5,7,6,4]
p = quick_sort(arr,0,len(arr)-1)
print(p)
