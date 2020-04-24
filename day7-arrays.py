'''Task
Given an array, arr, of n integers, print arr's elements in reverse order as a
single line of space-separated numbers.'''

n = int(input())

arr = list(map(int, input().rstrip().split()))

revarr=[]

lastindex=-1

for i in arr:
    revarr.append(arr[lastindex])
    lastindex-=1

print(*revarr, sep=' ')
