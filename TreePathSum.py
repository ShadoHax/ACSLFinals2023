import math
import os
import random
import re
import sys
# gg i forgot oop fucking kms gg idgaf anymore
tree = {}
# def maxtiersize (n):
#     return 2**(n-1)
def countUniqueSums(inputString):
    ilist = [int(i) for i in inputString]
    silist = sorted(ilist)
    # tier = 1
    rr = id(ilist[0])
    lr = id(ilist[0])
    for i in ilist:
        tree[id(i)] = []
        
    # if datatype is int iterate upwards until common parent node is found, check if actually common parent node with id()
        


countUniqueSums("31415926")