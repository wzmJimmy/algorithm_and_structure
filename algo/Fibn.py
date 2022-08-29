class Fibn_N:
    def __init__(self) -> None:
        self.memo = [1,1,2]
    
    def fibn(self,n):
        memo = self.memo
        while len(memo)<=n:
            memo.append(memo[-1]+memo[-2])
        return memo[n]

class Fibn_logN:
    def __init__(self) -> None:
        self.memo={0:1,1:1,2:2}
    def fibn(self,n):
        v = self.memo.get(n,None)
        if v: return v
        d,r = divmod(n,2)
        fh1,fh0 = self.fibn(d),self.fibn(d-1)
        res = fh1*(fh1+2*fh0) if r else fh1**2 + fh0**2
        self.memo[n] = res
        return res
if __name__ == "__main__":
    for i in [10,50,100,200,500,1000,3456,11086,2**16]:
        f1,f2 = Fibn_N(),Fibn_logN()
        v1,v2 = f1.fibn(i),f2.fibn(i)
        print(v1==v2,len(f2.memo),"{}..".format(str(v2)[:10]))
