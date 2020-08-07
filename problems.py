def findPairs(n, count=0, y=-1, i = 0):
    try:
        test = int(n)
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

    except ValueError:
        return "Please input an integer"
    except TypeError:
        return "Please input an integer"
    
def mergeList(nestedLis):
    if isinstance(nestedLis, list) == True:
        if len(nestedLis) == 0:
            return nestedLis
        if isinstance(nestedLis[0], list):
            return mergeList(nestedLis[0]) + mergeList(nestedLis[1:])
        else:
            return nestedLis[:1] + mergeList(nestedLis[1:])
    else:
        return "Please enter a list or nested list"

def recMin(nestedLis):
    nestedLis = mergeList(nestedLis)
    length = len(nestedLis)
    if length == 1:
        return nestedLis[0]
    else:
        minNum = recMin(nestedLis[1:])
        if minNum < nestedLis[0]:
            nestedLis[0] = minNum
        return nestedLis[0]
    
def addNext(n, count = 0):
    if n>0:
        count += n
        return addNext(n-2, count)
    else:
        return count

def swapElements(n, i = 0):
    length  = len(n) - 1
    if i < length:
        n[i], n[i+1] = n[i+1], n[i]
        i+=2
        return swapElements(n, i)
    else:
        return n

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
        return funkyNums(listToInteger(n), i)
    else:
        return listToInteger(n)

def calcStamp(cost, stampList, resultList = [], i=0 ):
    length = len(stampList) -1
    if i < length+1:
        if stampList[length-i] <= cost:
            resultList.append(stampList[length-i])
            cost-= stampList[length-i]
            i=0
            return calcStamp(cost, stampList, resultList, i)
        else:
            i+=1
            return calcStamp(cost, stampList, resultList, i)
    else:
        return "This order will require a minimum of " + str(len(resultList)) +" stamp(s)."+"\nthe denominations required are " + str(resultList)

def unitTest():
    print("Testing Find Pairs:")
    print("For input", 7645238, "should return 3,", findPairs(7645238))
    print("For input", 383838, "should return 0,", findPairs(383838))
    print("For input", 0, "should return 0,", findPairs(0))
    print("For input", 'ghsi', "should return 'Please input an integer',", findPairs('ghsi'))
    print("For input", [43,55,66], "should return 'Please input an integer',", findPairs([43,55,66]))

    print("\nTesting Merge List:")
    print("For input", [1,2,3,4,5], "should return [1,2,3,4,5],", mergeList([1,2,3,4,5]))
    print("For input", [], "should return [],", mergeList([]))
    print("For input", [66, [73,89,42,32], 62, [24, 32], 99 ], "should return [66,73,89,42,32,62,24,32,99],", mergeList([66, [73,89,42,32], 62, [24, 32], 99 ]))
    print("For input", [66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ], "should return [66, 73, 89, 23, 24, 88, 21, 22, 32, 44, 21, 42, 32, 62, 24, 32, 99],", mergeList([66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ]))
    print("For input", 'a string', "should return 'Please enter a list or nested list',", mergeList('a string'))
    print("For input", 12345, "should return 'Please enter a list or nested list',", mergeList(12345))

    print("\nTesting Rec Min:")
    print("For input", [66, [73,89,42,32], 62, [24, 32], 99 ], "should return 'Please enter a list or nested list',", recMin([66, [73,89,42,32], 62, [24, 32], 99 ]))


def main():
    unitTest()

if __name__ == "__main__":
    main()