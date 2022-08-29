from typing import List


""" scipy library using Hopcroft–Karp """
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
def maxmatching(grid: List[List[int]]) -> int:
    graph = csr_matrix(grid)
    res = maximum_bipartite_matching(graph)
    return sum(e >= 0 for e in res)

""" scipy general flow algorithm """
# from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
def maxmatching_flow(grid: List[List[int]]) -> int:
    m,n = len(grid),len(grid[0])
    new_grid = [[0]+[1]*m+[0]*(n+1)]
    for row in grid:
        new_grid.append([0]*(m+1)+row+[0])
    for _ in range(n):
        new_grid.append([0]*(m+n+1)+[1])
    new_grid.append([0]*(m+n+2))

    graph = csr_matrix(new_grid)
    return maximum_flow(graph,0,m+n+1).flow_value

""" Hopcroft–Karp """
# O(E*V^1/2)
# maximal set of vertex-disjoint shortest augmenting paths: (BFS + DFS)

from collections import deque
from math import inf, isinf
class HK:
    def __init__(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        self.pair_one = [None] * m
        self.pair_two = [None] * n
        self.graph = {}
        for i in range(m):
            se = set()
            for j in range(n):
                if grid[i][j]:
                    se.add(j)
            self.graph[i] = se

    # def BFS(self) -> bool:
    #     que = []
    #     dist = [inf] * len(self.pair_one)
    #     for i, v in enumerate(self.pair_one):
    #         if v is None:
    #             dist[i] = 0
    #             que.append(i)
    #     is_old = True
    #     while que and is_old:
    #         li = []
    #         for i in que:
    #             for j in self.graph[i]:
    #                 if self.pair_two[j] is None:
    #                     is_old = False
    #                     break
    #                 else:
    #                     inew = self.pair_two[j]
    #                     if isinf(dist[inew]):
    #                         dist[inew] = dist[i] + 1
    #                         li.append(inew)
    #         que = li
    #     self.dist = dist
    #     return not is_old

    def BFS(self) -> bool:
        dist_new, que = inf, deque()
        dist = [inf] * len(self.pair_one)
        for i, v in enumerate(self.pair_one):
            if v is None:
                dist[i] = 0
                que.append(i)

        while que:
            i = que.popleft()
            if dist[i] < dist_new:
                for j in self.graph[i]:
                    if self.pair_two[j] is None:
                        dist_new = dist[i] + 1
                        break
                    else:
                        inew = self.pair_two[j]
                        if isinf(dist[inew]):
                            dist[inew] = dist[i] + 1
                            que.append(inew)
        self.dist = dist
        return not isinf(dist_new)

    def _dfs_single(self, i: int) -> int:
        d = self.dist[i] + 1
        for j in self.graph[i]:
            i_new = self.pair_two[j]
            if i_new is None or (
                self.dist[i_new] == d and
                self._dfs_single(i_new)
            ):
                self.pair_one[i], self.pair_two[j] = j, i
                return True
        self.dist[i] = inf
        return False

    def DFS(self) -> int:
        res = 0
        for i, v in enumerate(self.pair_one):
            if v is None:
                res += self._dfs_single(i)
        return res

    def max_matching(self) -> int:
        match = 0
        while self.BFS():
            match += self.DFS()
        return match

# try to optimize and save dfs process. But find that this one may be slower in some case while not save too much coding
class HK2:
    def __init__(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        self.pair_one = [None] * m
        self.pair_two = [None] * n
        self.graph = {}
        for i in range(m):
            se = set()
            for j in range(n):
                if grid[i][j]:
                    se.add(j)
            self.graph[i] = se

    def BFS(self) -> bool:
        que,lfrom, ltop = [],[-1]*len(self.pair_one),[-1]*len(self.pair_one)
        for i, v in enumerate(self.pair_one):
            if v is None:
                ltop[i] = lfrom[i] = i
                que.append(i)

        new,top = {},set()
        while que and not new:
            li = []
            for i in que:
                for j in self.graph[i]:
                    if self.pair_two[j] is None:
                        if j not in new and ltop[i] not in top:
                            new[j] = i
                            top.add(ltop[i])
                            break
                    else:
                        inew = self.pair_two[j]
                        if lfrom[inew]<0:
                            lfrom[inew] = i
                            ltop[inew] = ltop[i]
                            li.append(inew)
            que = li
        self.lfrom,self.new = lfrom,new
        return bool(new)

    def augment(self) -> int:
        for j,i in self.new.items():
            while self.lfrom[i] != i:
                i_old,j_old = i,j
                j,i = self.pair_one[i],self.lfrom[i]
                self.pair_one[i_old], self.pair_two[j_old] = j_old,i_old
            self.pair_one[i], self.pair_two[j] = j, i
        return len(self.new)

    def max_matching(self) -> int:
        match = 0
        while self.BFS():
            # print(self.new,self.lfrom)
            match += self.augment()
        return match

if __name__ == "__main__":
    g1 = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]
    g2 = [[1, 0, 1, 0], [1, 0, 0, 0], [0, 0, 1, 0], [1, 1, 1, 0]]
    g3 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1], [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [
        0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1], [1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1], [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    for g in [g1,g2,g3]:
        print(f"Standard: {maxmatching(g)}, Standard_flow: {maxmatching_flow(g)}, HK: {HK(g).max_matching()}, HK2: {HK2(g).max_matching()}")