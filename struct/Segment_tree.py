from math import ceil, log2, inf
class Ops:
    ops = {
        "max" : lambda x,y: max(x,y),
        "add" : lambda x,y: x+y,
        "min" : lambda x,y: min(x,y)
    }
    default = {
        "max" : -inf,
        "add" : 0,
        "min" : inf
    }

class Seg_tree:
    @staticmethod
    def mid(s,e):
        return (s+e)//2 
    @staticmethod
    def left(i):
        return i*2+1 
    @staticmethod
    def maxsize(n):
        return 2**(ceil(log2(n))+1) - 1

    def __init__(self, arr, op = "max"):
        self.op = Ops.ops[op]
        self.default = Ops.default[op]
        self.n = len(arr)
        self.li = [0]*self.maxsize(self.n)
        self.build(arr,0,self.n-1)

    def build(self, arr, sid, eid, nid=0) :
        if sid == eid:
            self.li[nid] = arr[sid]
            return arr[sid]
        mid = self.mid(sid, eid)
        left = self.left(nid)
        v = self.li[nid] = self.op(
            self.build(arr,sid,mid,left),
            self.build(arr, mid+1,eid,left+1)
            )
        return v
    
    def get_range(self,qsid,qeid):
        assert(0<= qsid <= qeid < self.n)
        return self._get_range(0,self.n-1,qsid,qeid)

    def _get_range(self,sid,eid,qsid,qeid,nid=0):
        if qsid<=sid and qeid>=eid:
            return self.li[nid]
        if qsid>eid or qeid<sid:
            return self.default

        mid = self.mid(sid,eid)
        left = self.left(nid)
        return self.op(
            self._get_range(sid,mid,qsid,qeid,left),
            self._get_range(mid+1,eid,qsid,qeid,left+1)
        )

        
    def update(self,i,val):
        assert(0 <= i < self.n)
        return self._update(0,self.n-1,i,val)

    def _update(self,sid,eid,i,val,nid = 0):
        if i<sid or i>eid:
            return self.li[nid]
        if sid == eid:
            self.li[nid] = val
            return val
        
        mid = self.mid(sid, eid)
        left = self.left(nid)
        v = self.li[nid] = self.op(
            self._update(sid,mid,i,val,left),
            self._update(mid+1,eid,i,val,left+1)
            )
        return v


# Driver Code
if __name__ == "__main__" :
 
    arr = [1, 3, 5, 7, 9, 11]
    add_seg_tree = Seg_tree(arr,"add")
    print(add_seg_tree.li)

    tar = sum(arr[1:4])
    res = add_seg_tree.get_range(1,3)
    print(tar,res)
    assert(tar==res)
    arr[1] = 10
    add_seg_tree.update(1,10)
    tar = sum(arr[1:6])
    res = add_seg_tree.get_range(1,5)
    print(tar,res)
    assert(tar==res)

    arr = [7, 3, 2, 5, 11, 4]
    max_seg_tree = Seg_tree(arr,"max")
    print(max_seg_tree.li)

    tar = max(arr[:5])
    res = max_seg_tree.get_range(0,4)
    print(tar,res)
    assert(tar==res)
    arr[4] = 3
    max_seg_tree.update(4,3)
    tar = max(arr[:5])
    res = max_seg_tree.get_range(0,4)
    print(tar,res)
    assert(tar==res)
