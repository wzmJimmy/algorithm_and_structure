# # python indention validation
# #1,2,3,4

# """
# ans: True
# 123
# 1231:
#  313:
#    143:
#     123
#     21341
#   213
# 231
# epop == stack[-1] and idts!=stack[-1]
# epop > stack[-1] and idts!=stack[-1]
# """

# def count_idt(string):
#     c,l = 0,len(string)
#     while c<l and string[c]==' ': 
#         c += 1
#     return c
# def is_control(string):
#     return string and string[-1]==':'

# def python_valid(py_script:list(str))-> bool:
#     if not py_script or count_idt(py_script[0])!=0:
#         return False
    
#     stack,fcon = [0],False
#     for line in py_script:
#         idts = count_idt(line)
#         if fcon:
#             if idts<=stack[-1]: 
#                 return False
#         else:
#             while idts<stack[-1]:
#                 stack.pop()
#             if idts!=stack[-1]:
#                 return False
#         if idts!=stack[-1]:
#             stack.append(idts)
#         fcon = is_control(line)
#     return True
            



# We have a 2D skyline, where buildings are allowed to overlap or have gaps between.
# The goal is to compute the cross sectional area of skyline (without overcounting overlap).
# 
# Skyline illustration:
#              _____________                                      
#             |             |      
#             |             |        
#             |             |    
#      _ _    |             |        
#     |   |   |             |    
#     |   |   |          ___|___
#     |   |   |         |   |   |   
#  ___|___|___|_________|___|___|___
#     |   |   |         |   |   |
#     X   Y   A         B   C   D

# 0<start<end<limit
# [0,2,2,0,4] -> 8
import math 
from collections import deque
class Building:
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height



# [0,2,2,0,4] -> 8
from collections import defaultdict as dd
class Building:
    def __init__(self, start, end, height):
        self.start = start
        self.end = end
        self.height = height

        
def get_skyline_area(buildings):
    # todo: compute area
    li = []
    for build in buildings:
        li.append((build.start,build.height,build.end))
        li.append((build.end,build.height,build.end))
    li.sort()

    pos,now = dd(int),li[0][0]
    res = 0
    for x,h,e in li:
        if pos:
            res += (x-now) * max(pos.values())
        
        if x!=e:
            pos[e] = max(pos[e],h)
        else:
            if x in pos:
                del pos[x]
        now = x
        
    return res
            

def get_skyline_area(buildings):
    # todo: compute area
    li = []
    for build in buildings:
        li.append((build.start,build.height,True))
        li.append((build.end,build.height,False))
    li.sort()
#     buildings.sort(key = lambda b: (b.start,b.end))
    
    # list((h,e))
    mono,now = deque(),None
    res = 0
    # for b in buildings:
    #     if now is None:
    #         now = b.start
    #     # maintain
    #     while mono and mono[-1][0]<b.height and mono[-1][1]<b.end:
    #         mono.pop()
    #     mono.append((b.height,b.end))
    #     # caluclate
    #     if now!=b.start:
    #         while mono and mono[0][1]<b.start:
    #             mono.popleft()
    #         res += (b.start-now) * mono[0][0]
    for x,h,fs in li:
        if now is None:
            now = x
            mono.append((h,x))
        if fs:
            while mono and mono[0][1]<x:
                mono.popleft()
            res += (x-now) * mono[0][0]
            
            while mono and mono[-1][0]<h and mono[-1][1]<x:
                mono.pop()
            mono.append((h,x))
            now = x
        else:
            res += (x-now) * mono[0][0]
            if mono[0][1] == x:
                mono.popleft()
            now = x if mono else None
            
        
            
            
    
# Basic test case
buildings = [Building(1,3,2), Building(4,5,4)] # result should be 8
actual_result = get_skyline_area(buildings)

expected_result = 8
assert expected_result == actual_result, f"Actual result {actual_result}"
print("Passed!")