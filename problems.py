'''
Assignment 4: Recursion and Complexity
By: Cormac Doyle
Student Number: 20152002

This program includes 6 recursive problems (and any functions that they rely on) and
one computational complexity question. Each problem function has a description
explaining what it does.

Computational Complexity Question: (This question asks us to identify the complexity
of this mystery function and provide an explanation to our answer)

This function runs at roughly T(n) = 5n (5 operations within the for loop) + 2 (2 
operations outside the loop). This means the function has a big O of O(n) because
we take the n with the largest degree and don't worry about coefficients. The
program only has one loop which and the variable controlling the loop has not been
manipulated in any way because it is simply the length of the input list. This means
that the elements of the input list will only run once (worst case). Since for every
index, there is one new x. We can further prove that mystery() is an O(n) function 
by including a counter that counts every time the for loop in the function
runs. This counter will always be equal to the size of the inputted list. Therefore,
the loop runs only as many times as there are items in the input, which means the
function is linear or O(n).
'''
def mystery(lis):
    n = len(lis)

    for index in range(n):
        x = 2*index % n

        lis[index],lis[x] = lis[x],lis[index]

    print(lis)
'''
This function takes a non-negative integer as its paramater and returns the number of
pairs of numbers within the integer that sum to 10.
'''
def findPairs(n, count=0, y=-1, i = 0):
    try: # try except statement ensures that input is correct data type
        if n >= 0: #checks if inputted integer is 0 or a positive integer
            test = int(n) #this variable would trigger an error if the wrong data type was inputted
            length = len(str(n))
            iter_str = str(n)
            if i<length: #recursive case
                if y-i == -length:
                    #condition says that when all values have been checked against one, check all values for the next value
                    i+=1 #adds one to the index of the value being examined
                    y = -1 #resets the comparison value
                    return findPairs(iter_str, count, y, i)
                else:
                    if int(iter_str[i]) + int(iter_str[y]) == 10:
                        #checks to see if sum of pairs are in fact equal to 10
                        y-=1
                        count+=1 #adds to the total
                        return findPairs(iter_str, count, y, i)
                    else:
                        # if sum of pair in question is not equal to 10 check the value
                        y-=1
                        return findPairs(iter_str, count, y, i )
            else: #base case
                return count
        else: #if input is negative returns this error message
            return "Please enter a positive integer"

    except ValueError:
        return "Please input an integer"
    except TypeError:
        return "Please input an integer"

'''
This function accepts a list of lists called nestedLis as its parameter and returns
a single list containing all of the values in nestedLis.
'''
def mergeList(nestedLis):
    if isinstance(nestedLis, list) == True: #ensures that input is a list
        if len(nestedLis) == 0: #base case
            return nestedLis
        #recursive cases
        if isinstance(nestedLis[0], list):#checks if the index selected is a list
            return mergeList(nestedLis[0]) + mergeList(nestedLis[1:])
        else: #adds to stack and reduces size of input list
            return nestedLis[:1] + mergeList(nestedLis[1:])
    else: #if input is not a list raises this error message
        return "Please enter a list or nested list"
'''
This function accepts a list of lists called nestedLis as its parameter and returns
the smallest value in nestedLis.
'''
def recMin(nestedLis):
    if isinstance(nestedLis, list) == True: #ensures that input is a list
        nestedLis = mergeList(nestedLis) #cleans nested list to make it a list
        length = len(nestedLis)
        if length == 0: #checks for empty list input
            return None
        if length == 1: #base case
            return nestedLis[0]
        else: #recursive case
            minNum = recMin(nestedLis[1:]) 
            if minNum < nestedLis[0]: #checks to see if value is lower than previous lowest value
                nestedLis[0] = minNum
            return nestedLis[0]
    else: #if input is not a list returns this error message
        return "Please enter a list or nested list"
'''
This function takes a single integer n as its parameter and calculates the sum of
every other integer between 0 and n.
'''
def addNext(n, count = 0):
    if isinstance(n, int): #checks to see if input is an integer
        if n>0: #recursive case 
            count += n
            return addNext(n-2, count)
        else: #base case
            return count
    else:#if input is not an integer returns this error message
        return "Please enter an integer"
'''
This function accepts a list of integers as its parameter and returns a copy of
the list in which neighbouring elements have been swapped.
'''
def swapElements(listInput, i = 0):
    if isinstance(listInput, list) == True: #checks if input is a list
        length  = len(listInput) - 1
        if i < length: #recursive case
            listInput[i], listInput[i+1] = listInput[i+1], listInput[i] #swaps elements
            i+=2
            return swapElements(listInput, i)
        else: #base case
            return listInput
    else: #if input is not a list returns this error message
        return "Please enter a list"
'''
This function takes an integer as its parameter and returns a list in which each
element of that number is an individual list element.
'''
def integerToList(n): #helper function changes integer into a list for easier manipulation (allowed by Professor Allison)
    n = str(n) #turns int to string
    newlist = []
    for i in n:
        newlist.append(i)
    return newlist # returns list with each number in the integer as a list element
'''
This function takes a list of integers as its parameter and returns an integer
of those values combined.
'''
def listToInteger(alist): #helper function changes list into an integer for easier manipulation (allowed by Professor Allison)
    string = ""
    string = string.join(alist)
    return int(string) #returns integer
'''
This function accepts a positive integer as its parameter and returns the integer
backwards.
'''
def funkyNums(n, i=0):
    if isinstance(n, int) == True:#checks to make sure input is an integer
        n = integerToList(n) # converts integer into list
        length = len(n) - 1
        #recursive case
        if i < length//2: # each iteration deals with 2 elements so we only deal with the index for half of the list
            n[i], n[length-i] = n[length-i], n[i]
            i+=1
            return funkyNums(listToInteger(n), i)
        else: #base case
            return listToInteger(n)
    else:#if input is not an integer returns this error message
        return "Please enter an integer"
'''
This function returns the minimum number of stamps that would be required in order
to pay the postage cost, the function accepts a postage cost and a list of integers
representing the stamp denominations as its parameters.
'''
def calcStamp(cost, stampList, resultList = None, i=0 ):
    if isinstance(cost, int) == True and isinstance(stampList, list) == True: #checks if cost is integer and stamp list is list
        if resultList is None: #clears resultList from last function call
            resultList = []
        length = len(stampList) -1
        if i < length+1: #recursive case
            if stampList[length-i] <= cost: #checks for closest value less than or equal to cost
                resultList.append(stampList[length-i]) #adds highest value to result list
                cost-= stampList[length-i]  #changes cost variable to outstanding cost balance
                i=0 #resets index value
                return calcStamp(cost, stampList, resultList, i)
            else:
                i+=1 #checks next largest value
                return calcStamp(cost, stampList, resultList, i)
        else:#base case
            return len(resultList) 
    else: #if cost is not integer and stamp list is not a list return this error message
        return "Invalid, please enter an integer followed by a list"
'''
Test function shows what should be returned for a function for a given output and
what the function actually outputs.
'''
def unitTest():
    print("Testing Find Pairs:")
    print("For input", 7645238, ",should return 3,", findPairs(7645238))
    print("For input", 383838, ",should return 0,", findPairs(383838))
    print("For input", 0, ",should return 0,", findPairs(0))
    print("For input", -7645238, ",should return Please enter a positive integer,", findPairs(-7645238))
    print("For input", 'ghsi', ",should return 'Please input an integer',", findPairs('ghsi'))
    print("For input", [43,55,66], ",should return 'Please input an integer',", findPairs([43,55,66]))

    print("\nTesting Merge List:")
    print("For input", [1,2,3,4,5], ",should return [1,2,3,4,5],", mergeList([1,2,3,4,5]))
    print("For input", [], ",should return [],", mergeList([]))
    print("For input", [66, [73,89,42,32], 62, [24, 32], 99 ], ",should return [66,73,89,42,32,62,24,32,99],", mergeList([66, [73,89,42,32], 62, [24, 32], 99 ]))
    print("For input", [66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ], ",should return [66, 73, 89, 23, 24, 88, 21, 22, 32, 44, 21, 42, 32, 62, 24, 32, 99],", mergeList([66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ]))
    print("For input", 'a string', ",should return 'Please enter a list or nested list',", mergeList('a string'))
    print("For input", 12345, ",should return 'Please enter a list or nested list',", mergeList(12345))

    print("\nTesting Rec Min:")
    print("For input", [66, [73,89,42,32], 62, [24, 32], 99 ], ",should return 24,", recMin([66, [73,89,42,32], 62, [24, 32], 99 ]))
    print("For input", [66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ], ",should return 21,", recMin([66, [73,89,[23,24,88,[21,22,32,44],21],42,32], 62, [24, 32], 99 ]))
    print("For input", [], "should return None,", recMin([]))
    print("For input", 'This String', ",should return Please enter a list or nested list,", recMin('This String'))
    print("For input", 5, ",should return Please enter a list or a nested list,", recMin(5))

    print("\nTesting Add Next:")
    print("For input", 6, ",should return 12,", addNext(6))
    print("For input", 8, ",should return 20,", addNext(8))
    print("For input", 0, ",should return 0,", addNext(0))
    print("For input", 'This string', ",should return Please enter an integer,", addNext('This string'))
    print("For input", [42,21,22], ",should return Please enter an integer,", addNext([41,21,22]))

    print("\nTesting Swap Elements:")
    print("For input", [3,8,2,1], ",should return [8,3,1,2],", swapElements([3,8,2,1]))
    print("For input", [3,8,2,1,5], ",should return [8,3,1,2,5],", swapElements([3,8,2,1,5]))
    print("For input", [], ",should return [],", swapElements([]))
    print("For input", 'This String', ",should return Please enter a list,", swapElements('This String'))
    print("For input", 5, ",should return Please enter a list,", swapElements(5))

    print("\nTesting Funky Nums:")
    print("For input", 5637, ",should return 7365,", funkyNums(5637))
    print("For input", 56379, ",should return 97365,", funkyNums(56379))
    print("For input", 0, ",should return 0,", funkyNums(0))
    print("For input", "This String", ",should return Please enter an integer,", funkyNums("This String"))
    print("For input", [55,32,21], ",should return Please enter an integer,", funkyNums([55,32,21]))

    print("\nTesting Calc Stamps:")
    print("For input", 11, [1, 2, 5, 12, 14, 18], ",should return 3,", calcStamp(11, [1, 2, 5, 12, 14, 18]))
    print("For input", 19, [1, 2, 5, 12, 14, 18], ",should return 1,", calcStamp(18, [1, 2, 5, 12, 14, 18]))
    print("For input", [1, 2, 5, 12, 14, 18], 19,",should return Invalid, please enter an integer followed by a list", calcStamp([1, 2, 5, 12, 14, 18], 19))
    print("For input", 'This List', 0, ",should return Invalid, please enter an integer followed by a list,", calcStamp('This list', 0))

def main():
    unitTest()

if __name__ == "__main__":
    main()