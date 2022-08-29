def KMP_table(st):
    l = len(st)
    jump = [-1] + [0]*(l)
    for i in range(1,l+1):
        j,pre = jump[i-1],st[i-1]
        while j>=0 and st[j] != pre:
            j = jump[j]
        jump[i] = j+1
    
    for i in range(1,l):
        j = jump[i]
        while j>=0 and st[j]==st[i]:
            j = jump[j]
        jump[i] = j
    return jump

def bsc_kmp(a,b):
    jump = KMP_table(b)
    l1,l2 = len(a),len(b)
    i1 = i2 = 0
    while i1<l1 and i2<l2:
        if a[i1]==b[i2]:
            i1 += 1
            i2 += 1
        else:
            i2 = jump[i2]
            if i2<0:
                i2 = 0
                i1 += 1
    return i2==l2

if __name__ == "__main__":
    li = [("asvasvsd","sd"),
    ("sadfasfasfdsfasdfsadfsdfsfsvregebethqvf","fsvreg"),
    ("sfaswf","agawvaergavergq"),
    ("sdwgvwvgwgqaebvqagvaewrgqawv","212312313sdvasdvsa")]

    for a,b in li:
        print(bsc_kmp(a,b),b in a)