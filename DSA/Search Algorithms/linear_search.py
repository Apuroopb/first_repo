# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search(l,a):
    for i in range(0,len(l)):
        if(l[i]==a):
            return i
    return -1

l=[3,2,3,5,6,3,4,5,6,9,7,1]
a=11
print(linear_search(l,a))
