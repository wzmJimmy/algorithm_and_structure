from abc import ABC, abstractmethod
""" # Trie Tree # """
class TrieABC(ABC):
    @abstractmethod
    def search(self,word):
        pass
    @abstractmethod
    def add(self,word):
        pass
    # @abstractmethod
    # def delete(self,word):
    #     pass

class TrieNodeBase:
    def __init__(self,val=None) -> None:
        self.val = val
        self.next = {}

class BasicTrie:
    def __init__(self):
        self.head = TrieNodeBase()

    def search(self, word):
        l,i,now = len(word),0,self.head
        while i<l:
            c = word[i]
            if c in now.next:
                i += 1
                now = now.next[c]
            else: break
        return (i,now)
    
    def add(self, word):
        i,nod = self.search(word)
        for j in range(i,len(word)):
            c = word[j]
            nod.next[c] = nod = TrieNodeBase()
        nod.val = word


class CompressTrie(TrieABC):
    def __init__(self):
        self.head = TrieNodeBase()

    def search(self, word):
        l,i,now = len(word),0,self.head
        while i<l:
            c = word[i]
            if c in now.next:
                i += 1
                now = now.next[c]
            else: break
        return (i,now)
    
    def add(self, word):
        i,nod = self.search(word)
        if not nod.val:
            if i==len(word):
                nod.val = word
            else:
                nod.next[word[i]] = TrieNodeBase(word)
        elif nod.val != word:
            w2,nod.val = nod.val,None
            l1,l2 = len(word),len(w2)
            l = min(l1,l2)

            while i<l and w2[i] == word[i]:
                nod.next[word[i]] = nod = TrieNodeBase()
                i += 1
            dic = nod.next

            if i!=l:
                dic[word[i]],dic[w2[i]] = TrieNodeBase(word),TrieNodeBase(w2)
            elif i==l1:
                dic[w2[i]],nod.val = TrieNodeBase(w2),word
            else:
                dic[word[i]],nod.val = TrieNodeBase(word),w2

# class BasicTrie(TrieABC):
#     def __init__(self):
#         self.head = TrieNodeBase()

#     def search(self, word):
#         l,i,now = len(word),0,self.head
#         while i<l:
#             c = word[i]
#             if c in now.next:
#                 i += 1
#                 now = now.next[c]
#             else: break
#         return (i,now)
    
#     def add(self, word):
#         i,nod = self.search(word)
#         for j in range(i,len(word)):
#             c = word[j]
#             nod.next[c] = nod = TrieNodeBase()
#         nod.val = word
    
#     def delete(self, word):
#         st = [self.head]
#         for i,c in enumerate(word):
#             if c not in st[-1].next: 
#                 return False
#             st.append(st[-1].next[c])

#         nod = st.pop()
#         nod.val = None
#         if nod.next: return True

#         for c in word[::-1]:
#             nod = st.pop()
#             del nod.next[c]
#             if nod.val is not None or nod.next: break 
#         return True
              
#     def prefix(self,pre,first=True,sort=True):
#         i,nod = self.search(pre)
#         if i!=len(pre): return None
#         if first:
#             while nod.val is None:
#                 c = min(nod.next)
#                 nod = nod.next[c]
#             return nod.val
#         res = []
#         def traverse(node):
#             if node.val: res.append(node.val)
#             dic = node.next
#             if sort:
#                 for k in sorted(dic.keys()):
#                     traverse(dic[k])
#             else:
#                 for v in dic.values():
#                     traverse(v)
#         traverse(self.head)
#         return res

#     def check(self,word):
#         i,nod = self.search(word)
#         return i==len(word) and nod.val is not None

#     def print(self):
#         li = []
#         def dfs(node):
#             if node.val: li.append(node.val)
#             dic = node.next
#             for k in sorted(dic.keys()):
#                 li.append(k)
#                 dfs(dic[k])
#         dfs(self.head)
#         print(li)


# class CompressTrie(TrieABC):
#     def __init__(self):
#         self.head = TrieNodeBase()

#     def search(self, word):
#         l,i,now = len(word),0,self.head
#         while i<l:
#             c = word[i]
#             if c in now.next:
#                 i += 1
#                 now = now.next[c]
#             else: break
#         return (i,now)
    
#     def add(self, word):
#         i,nod = self.search(word)
#         if not nod.val:
#             if i==len(word):
#                 nod.val = word
#             else:
#                 nod.next[word[i]] = TrieNodeBase(word)
#         elif nod.val != word:
#             w2,nod.val = nod.val,None
#             l1,l2 = len(word),len(w2)
#             l = min(l1,l2)

#             while i<l and w2[i] == word[i]:
#                 nod.next[word[i]] = nod = TrieNodeBase()
#                 i += 1
#             dic = nod.next

#             if i!=l:
#                 dic[word[i]],dic[w2[i]] = TrieNodeBase(word),TrieNodeBase(w2)
#             elif i==l1:
#                 dic[w2[i]],nod.val = TrieNodeBase(w2),word
#             else:
#                 dic[word[i]],nod.val = TrieNodeBase(word),w2

    
#     def delete(self, word):
#         st = [self.head]
#         for i,c in enumerate(word):
#             if c not in st[-1].next: 
#                 if st[-1].val!=word: return False
#                 break
#             st.append(st[-1].next[c])

#         nod = st.pop()
#         nod.val = None
#         if nod.next: return True

#         first,end = True,None
#         for c in word[i-1::-1]:
#             nod = st.pop()
#             del nod.next[c]
#             if first:
#                 if len(nod.next)>1: break
#                 if nod.next:
#                     end = nod.next.popitem()[1]
#                 first = False
#             elif nod.val is not None or nod.next: 
#                 if end: nod.next[c] = end 
#                 break 
#         return True
              
#     def prefix(self,pre,first=True,sort=True):
#         i,nod = self.search(pre)
#         if i!=len(pre):
#              if not nod.val or not nod.val.startswith(pre): return None
#              return nod.val if first else [nod.val]

#         if first:
#             while nod.val is None:
#                 c = min(nod.next)
#                 nod = nod.next[c]
#             return nod.val

#         res = []
#         def traverse(node):
#             if node.val: res.append(node.val)
#             dic = node.next
#             if sort:
#                 for k in sorted(dic.keys()):
#                     traverse(dic[k])
#             else:
#                 for v in dic.values():
#                     traverse(v)
#         traverse(self.head)
#         return res

#     def check(self,word):
#         i,nod = self.search(word)
#         return word==nod.val

#     def print(self):
#         li = []
#         def dfs(node):
#             if node.val: li.append(node.val)
#             dic = node.next
#             for k in sorted(dic.keys()):
#                 li.append(k)
#                 dfs(dic[k])
#         dfs(self.head)
#         print(li)


"""
# class JNode(TrieNodeBase):
#     def __init__(self, val=None):
#         self.jump = None
#         super().__init__(val=val)

# from collections import deque
# class KMP_Trie(TrieABC):
#     def __init__(self):
#         self.head = JNode()

#     def search(self, word):
#         l,i,now = len(word),0,self.head
#         while i<l:
#             c = word[i]
#             if c in now.next:
#                 i += 1
#                 now = now.next[c]
#             else: break
#         return (i,now)

#     def add(self, word):
#         i,nod = self.search(word)
#         for j in range(i,len(word)):
#             c = word[j]
#             nod.next[c] = nod = JNode()
#         nod.val = word

#     def build_jump_tree(self):
#         que = deque([self.head])
#         while que:
#             nod = que.popleft()
#             for c,v in nod.next.items():
#                 # Build jump
#                 j = nod.jump
#                 while j and c not in j.next:
#                     j = j.jump
#                 v.jump = j.next[c] if j else self.head

#                 que.append(v)

#     def print(self):
#         li = []
#         def dfs(node):
#             if node.val: li.append(node.val)
#             dic = node.next
#             for k in sorted(dic.keys()):
#                 n = node.next[k]
#                 li.append((k,list(n.jump.next.keys()) if n.jump else None))
#                 dfs(dic[k])
#         dfs(self.head)
#         print(li)
    


# tree = KMP_Trie()
# tree.add("aab")
# tree.add("abb")
# tree.add("cda")
# tree.add("abbcda")
# tree.add("abbccd")
# tree.print()
# tree.build_jump_tree()
# tree.print()
"""

# if __name__ == "__main__":
    # tree = BasicTrie()
    # # tree = CompressTrie()
    # tree.add("aab")
    # tree.print()
    # tree.add("abb")
    # tree.print()
    # tree.add("cda")
    # tree.print()
    # tree.add("abbcda")
    # tree.print()
    # tree.add("abbccd")
    # tree.print()

    # print(tree.check("aab"))
    # print(tree.check("abbccd"))
    # print(tree.check("w"))

    # print(tree.prefix("d"))
    # print(tree.prefix("a"))
    # print(tree.prefix("a",False,False))
    # print(tree.prefix("a",False))

    # print(tree.delete("ae"))
    # print(tree.delete("abbccd"))
    # print(tree.prefix("a",False))
    # print(tree.delete("abb"))
    # print(tree.prefix("a",False))
