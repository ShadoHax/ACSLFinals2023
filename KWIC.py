import math
import os
import random
import re
import sys
# gg idgaf whatever man
punctuation = [".", "?", "!", ",", ";", ":"]
repeats = []
priorMASTER = []
postMASTER = []
wordMASTER = []
priorLEN = []
postLEN = []

def setSeeker(ilist, word):
    if word not in repeats:
        return ilist.index(word)
    else:
        return ilist[[i for i, n in enumerate(ilist) if n == word][repeats.count(word)-1]:].index(word) + [i for i, n in enumerate(ilist) if n == word][repeats.count(word)]

def findARow(original, unused, rows):
    olist = original.split()
    ulist = unused.split()
    solist = sorted(olist, key=str.lower)
    # create a way to map repeat to its location then set seeker to the next index after that split from the repeat
    for item in solist:
        flag = True
        if item.lower() in ulist:
            flag = False
        if flag:
            seeker = setSeeker(olist, item)
            otem = item
            for stripper in punctuation:
                if stripper in item:
                    otem = item.strip(stripper)
            priors = []
            posts = []
            for j in range(seeker-1, seeker-4, -1):
                ck = olist[j]
                if ck.lower() in ulist or ck[-1] in punctuation:
                    # print(f"{ck} is in {ulist} or {ck[-1]} is in punc")
                    break
                priors.insert(0, ck)
            for k in range(seeker+1, seeker+4):
                if item[-1] in punctuation:
                    break
                ck = olist[k]
                if ck.lower() in ulist or ck[-1] in punctuation:
                    break
                posts.append(ck)
            fpriors = 0
            fposts = 0
            if len(priors) > 0:
                fpriors = len(priors) - 1
            if len(posts) > 0:
                fposts = len(posts) - 1
            priorMASTER.append(priors)
            priorLEN.append(sum([len(i) for i in priors]) + fpriors)
            # print("priors, posts", priors, f"||{item}||", posts)
            postMASTER.append(posts)
            postLEN.append(sum([len(i) for i in posts]) + fposts)
            wordMASTER.append(otem)
            repeats.append(item)
    maxprior = max(priorLEN)
    print(maxprior, priorMASTER[priorLEN.index(maxprior)])
    maxword = max([len(i) for i in wordMASTER])
    print(maxword, wordMASTER[[len(i) for i in wordMASTER].index(maxword)])
    maxpost = max(postLEN)
    # print(postMASTER)
    print(maxpost, postMASTER[postLEN.index(maxpost)])
    rowmap = [0 for i in priorMASTER]
    # print(maxprior, maxword, maxpost)
    for i in range(len(priorMASTER)):
        # print(maxprior - len(priorLEN[i]), maxword - len(wordMASTER[i]), maxpost - len(postMASTER[i]))
        rowmap[i] = (maxprior - priorLEN[i]) + (maxword - len(wordMASTER[i])) + (maxpost - postLEN[i])
        # print(rowmap[i], i)
    # print(rowmap[int(rows.split()[0]):int(rows.split()[1]) + 1])
    rindex = rowmap.index(min(rowmap[int(rows.split()[0]) - 1:int(rows.split()[1]) + 1]))
    
    # for i in range(len(priorMASTER)):
    #     print(priorMASTER[i], wordMASTER[i], postMASTER[i])
    priorout = ""
    wordout = "<" + wordMASTER[rindex]
    postout = ""
    for i in range(len(postMASTER[rindex])):
        postout += postMASTER[rindex][i]
        if i != len(postMASTER[rindex]) - 1:
            postout += " "
    for i in range(maxprior - priorLEN[rindex]):
        priorout += "-"
    for i in range(len(priorMASTER[rindex])):
        priorout += priorMASTER[rindex][i]
        if i != len(priorMASTER[rindex]) - 1:
            priorout += " "
    for i in range(maxword - len(wordMASTER[rindex])):
        wordout += "-"
    wordout += ">"
    for i in range(maxpost - postLEN[rindex]):
        postout += "-"
    result = priorout + " " + wordout + " " + postout
    # return result
    print(rindex, wordMASTER[rindex])
    print(result)
    # NOTE each word comes with a +1 space? no only between them
    # add each set as a string and then just have it subtract the length of the string from the longest and just format at the final stage
    # make sure all are in order and just have them all pair
    # seeker
findARow("Lions and Tigers and Bears, Oh My! is from the Wizard of Oz. Where is it found?", "and from the it", "1 10")
# for i in range(len(priorMASTER)):
#     print(priorMASTER[i], wordMASTER[i], postMASTER[i])
