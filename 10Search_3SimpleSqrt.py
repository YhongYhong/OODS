def bi_search(l, r, arr, x):
    # print(l, r)
    while l <= r:
        mid = (l + r)//2
        # print(mid, x)
        if mid*mid < x and (mid+1)*(mid+1) <= x:
            l = mid+1
        elif mid*mid > x or (mid-1)*(mid-1) > x:
            r = mid-1
        else:
            l = r+1
    
    # print(x ,mid)
    if x >= mid*mid:
        return mid
    else:
        return -1

inp = int(input("simple sqrt: "))
print(bi_search(0, inp//2, None, inp))