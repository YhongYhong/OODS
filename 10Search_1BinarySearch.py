def bi_search(l, r, arr, x):
    # Code Here
    while l <= r:
        mid = (l + r)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
        else:
            l = r+1
    
    if x == arr[mid]:
        return True
    else:
        return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))