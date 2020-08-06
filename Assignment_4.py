def findPairs(n, count=0, y=-1, i = 0):
    length = len(str(n))
    iter_str = str(n)
    #print(i, y, length)
    if i<length:
        if y-i == -length:
            i+=1
            y = -1
            return findPairs(iter_str, count, y, i)
        else:
            if int(iter_str[i]) + int(iter_str[y]) == 10:
                y-=1
                count+=1
                return findPairs(iter_str, count, y, i)
            else:
                y-=1
                return findPairs(iter_str, count, y, i )
    else:
        return count

#print("There are", findPairs(7645238), "pairs of 10 in the number")

def mergeList(nestedLis, n=0, cleanLis = [], i=0):
    if n == len(nestedLis):
        return cleanLis
    else:
        if isinstance(nestedLis[n], list) == True:
            if i< len(nestedLis[n]):
                cleanLis.append(nestedLis[n][i])
                i+=1
                return mergeList(nestedLis, n, cleanLis, i)
            else:
                n+=1
                return mergeList(nestedLis, n, cleanLis)
        else:
            print("MAAAAAN")
            cleanLis.append(nestedLis[n])
            n+=1
            return mergeList(nestedLis, n, cleanLis)

#print(mergeList([66,[73,[89,42],32],62,[24,32],99]))

def addNext(n, count = 0):
    if n>0:
        count += n
        return addNext(n-2, count)
    else:
        return count

#print(addNext(6))

def swapElements(n, i = 0):
    length  = len(n) - 1
    if i < length:
        n[i], n[i+1] = n[i+1], n[i]
        i+=2
        return swapElements(n, i)
    else:
        return n
#print(swapElements([]))

def integerToList(n):
    n = str(n)
    newlist = []
    for i in n:
        newlist.append(i)
    return newlist

def listToInteger(n):
    string = ""
    string = string.join(n)
    return int(string)

def funkyNums(n, i=0):
    n = integerToList(n)
    length = len(n) - 1
    if i < length//2:
        n[i], n[length-i] = n[length-i], n[i]
        i+=1
        print(n, i)
        return funkyNums(listToInteger(n), i)
    else:
        return n
print(funkyNums(73656))