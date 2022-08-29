def lastbit(i): return i & -i
def parent(i): return i & (i - 1)   # parent(i) = i - lastbit(i)
def nextpow(i): return i + lastbit(i) # (i | (i - 1)) + 1
from math import log2,floor



class BIT:
    def __init__(self,li=None):
        if not li:
            self.li = []
        else:
            self.li = [0] + li
            self.build()

    def build(self): #O(N)
        l = len(self.li)
        for i in range(1,l):
            j = nextpow(i)
            if j<l: self.li[j] += self.li[i]

    def adjust(self,i,dv):
        l = len(self.li)
        while i<l:
            self.li[i] += dv
            i = nextpow(i)

    def prefixsum(self,i):
        su = 0
        while i > 0:
            su += self.li[i]
            i = parent(i)
        return su

    def rangesum(self,i,j):
        su = 0
        while j > i:
            su += self.li[j]
            j = parent(j)
        while i > j:
            su -= self.li[i]
            i = parent(i)
        return su

    def rankq(self,k):
        i,l = 0,len(self.li)-1
        j = 1 << floor(log2(l))
        while j:
            ind = i+j
            if ind<=l and self.li[ind]<=k:
                k -= self.li[ind]
                i = ind
            j >>= 1
        return ind

    def append(self,v):
        i = len(self.li)
        self.li.append(v)
        lb = lastbit(i) >> 1
        while lb:
            self.li[-1] +=  self.li[i-lb]
            lb >>= 1

    # operations without original list
    def reverse(self):
        l,li = len(self.li),[i for i in self.li]
        for i in range(l-1,0,-1):
            j = nextpow(i)
            if j<l: li[j] -= li[i]
        return li

    def get(self,i):
        return self.rangesum(i-1,i)
    def replace(self,i,v):
        self.adjust(i,v-self.get(i))


    

    

