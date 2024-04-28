def bi_search(l, r, arr, x):
    # Code Here
    # print(arr)
    while l <= r:
        mid = (l + r)//2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
        else:
            l = r+1
    # print(mid, r, l)
    if arr[mid] <= x and mid+1 <= len(arr)-1:
        return arr[mid+1]
    elif arr[mid] > x:
        return arr[mid]
    else:
        return "No First Greater Value"

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), list(map(int,inp[1].split()))
# print(arr, sorted(arr), k)
for i in k:
    print(bi_search(0, len(arr) - 1, sorted(arr), i))