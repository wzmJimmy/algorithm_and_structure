class Ndll:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.nxt = None
# class DLL:
#     def __init__(self):
#         self.head = self.tail = None

#     def append(self,nod):
#         if not self.head:
#             self.head = nod
#         else:
#             self.tail.nxt,nod.pre = nod,self.tail
#         self.tail = nod

#     def remove(self,n):
#         # n must inside this DLL
#         if self.head==self.tail:
#             self.head=self.tail=None
#             return n
#         l,r = n.pre,n.nxt
#         if n==self.tail:
#             self.tail = l
#             l.nxt = n.pre = None
#         if n==self.head:
#             self.head = r
#             r.pre = n.nxt = None
#         else:
#             l.nxt,r.pre = r,l
#             n.nxt = n.pre = None
#         return n

#     def movetoright(self,n):
#         # n must inside this DLL
#         if n == self.tail: return
#         self.remove(n)
#         self.append(n)


class DLL:
    def __init__(self):
        self.pre = Ndll(None)
        self.suf = Ndll(None)
        self.pre.nxt = self.suf
        self.suf.pre = self.pre

    def append(self, nod):
        tail, suf = self.suf.pre, self.suf
        tail.nxt = suf.pre = nod
        nod.pre, nod.nxt = tail, suf

    def remove(self, n):
        # n must inside this DLL
        pre, suf = n.pre, n.nxt
        pre.nxt, suf.pre = suf, pre
        n.pre = n.nxt = None

    def movetoright(self, n):
        # n must inside this DLL
        if n == self.suf.pre:
            return
        self.remove(n)
        self.append(n)

    @property
    def head(self):
        nod = self.pre.nxt
        return None if self.suf == nod else nod

    @property
    def tail(self):
        nod = self.suf.pre
        return None if self.pre == nod else nod
