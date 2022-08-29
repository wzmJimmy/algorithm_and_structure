
def bs_ex(li,tar):
    s,e = 0,len(li)-1
    while s<e:
        mid = (s+e)//2
        if li[mid]==tar: return mid
        if li[mid]< tar:
            s = mid + 1
        else:
            e = mid - 1
    return -1 

def bs_left(li,tar): 
    # give the leftmost index with number >= target
    if not li or li[0]>=tar: 
        return 0 
    if li[-1]< tar:
        return len(li)

    s,e = 0,len(li)-1
    while s<e:
        mid = (s+e)//2
        if li[mid]< tar:
            s = mid + 1
        else:
            e = mid
    return s 

def bs_right(li,tar):
    # give left-most index with number > target
    if not li or li[0]>tar: 
        return 0 
    if li[-1]<= tar:
        return len(li)

    s,e = 0,len(li)-1
    while s<e:
        mid = (s+e)//2
        if li[mid]<= tar:
            s = mid + 1
        else:
            e = mid
    return s 

l1 = []
#     0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
l2 = [1,1,2,3,4,4,4,5,6,6,6,7,10,11,11,11]
print(bs_ex(l1,1),bs_ex(l2,6),l2[bs_ex(l2,6)],bs_ex(l2,8))
print(bs_left(l1,1),bs_right(l1,1))
print(bs_left(l2,8),bs_right(l2,8))
print(bs_left(l2,6),bs_right(l2,6))
print(bs_left(l2,1),bs_right(l2,1))
print(bs_left(l2,11),bs_right(l2,11))


