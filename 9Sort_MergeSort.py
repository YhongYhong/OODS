def mergeSort(l, left, right):
    center = (left+right)//2
    print(left, right, center)
    if left < right:
        mergeSort(l, left, center)
        print('go right', l)
        mergeSort(l, center+1, right)
        print('go in merge', l)
        merge(l, left, center+1, right)
        
def merge(l, left, right, rightEnd):
    start = left
    leftEnd = right-1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1
        
    for ele in result:
        l[start] = ele
        start += 1
        if start > rightEnd:
            break

l = [5,3,6,1,2,7,8,4]
print(l)
mergeSort(l, 0, len(l)-1)
print(l)