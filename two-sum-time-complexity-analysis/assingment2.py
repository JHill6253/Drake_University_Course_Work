from timeit import default_timer as timer
import random
import matplotlib.pyplot as plt
import sys
sys.stdout = open('/Users/a1565502/Documents/School/CS 137/assingment2Table.txt', 'w')
#Brute Force Implomentation:
def BruteForce(s1,s2,x):
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]+s2[j] == x:
                return True 
    return False


#Binary Search Implomentation 
def BinarySearch(s1,s2,x):
    s2.sort()
    for i in range(len(s1)):
        low = 0
        high = len(s2)-1
        potentialMatch = x-s1[i]
        isMatch = BinarySearchUtility(s2,potentialMatch, low, high)
        if isMatch ==True:
            return True 
    return False 


# Actual Binary Search Function 
def BinarySearchUtility(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return True 
        elif arr[mid] > target:
            return BinarySearchUtility(arr,target, low, mid - 1)
        else:
            return BinarySearchUtility(arr,target, mid +1, high)
    else:
        return False 

#HashSet Implomentation
def HashSet(s1,s2,target):
    h2 = set(s2)
    for i in range(len(s1)):
        potentialMatch = target - s1[i]
        if potentialMatch in h2:
            return True 
    return False
    
#Sorting and Sweeping 
def SortingAndSweeping(s1,s2,target): 
    s1.sort()
    s2.sort()
    l = 0 
    r = len(s1)-1
    while l <= r:
        potentialSum =  s1[l]+s2[r]
        if potentialSum == target:
            return True 
        if potentialSum <= target:
            l +=1
        if potentialSum >= target: 
            r -=1
    return False

# Create random inputs for array
def CreateInputArray(n):
    return [random.randint(1,1000) for _ in range(n)]


#Clocks time each function took to complete 
def GetTime(function, s1,s2,x):
    start_time = timer()
    function(s1,s2,x)
    end_time = timer()
    total_time = end_time - start_time
    return total_time

# Test case class to store vars to be used in experiments 
class testCase:
    def __init__(self, n):
        self.len = n
        self.s1 = CreateInputArray(n)
        self.s2 = CreateInputArray(n)
        self.target = random.randint(0,100)
        self.brute = GetTime(BruteForce,self.s1,self.s2,self.target)
        self.binary = GetTime(BinarySearch,self.s1,self.s2,self.target)
        self.hash = GetTime(HashSet,self.s1,self.s2,self.target)
        self.sweep = GetTime(SortingAndSweeping,self.s1,self.s2,self.target)

# arrays containg data to be plotted 
n = []
brute = []
binary = []
hash = []
sweep = []
for i in range(100,10100,100 ):
    n.append(testCase(i).len)
    brute.append(testCase(i).brute)
    binary.append(testCase(i).binary)
    hash.append(testCase(i).hash)
    sweep.append(testCase(i).sweep)


plt.plot(n, brute)
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Brute Force')
plt.show()
plt.plot(n, binary)
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Binary Search')
plt.show()
plt.plot(n, hash)
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Hash Set')
plt.show()
plt.plot(n, sweep)
plt.xlabel('N')
plt.ylabel('Time')
plt.title('Sorting and Sweeping')
plt.show()

plt.plot(n, binary, label = "Binary Search")
plt.plot(n, sweep, label = "Sorting and Sweeping")
plt.plot(n, hash, label = "Hash Set")
 
plt.xlabel('N')
plt.ylabel('Time')
plt.title('All Solutions not brute force')
plt.legend()
plt.show()


def makeTable(headerRow,columnizedData,columnSpacing=2):
    from numpy import array,max,vectorize

    cols = array(columnizedData,dtype=str)
    colSizes = [max(vectorize(len)(col)) for col in cols]

    header = ''
    rows = ['' for i in cols[0]]

    for i in range(0,len(headerRow)):
        if len(headerRow[i]) > colSizes[i]: colSizes[i]=len(headerRow[i])
        headerRow[i]+=' '*(colSizes[i]-len(headerRow[i]))
        header+=headerRow[i]
        if not i == len(headerRow)-1: header+=' '*columnSpacing

        for j in range(0,len(cols[i])):
            if len(cols[i][j]) < colSizes[i]:
                cols[i][j]+=' '*(colSizes[i]-len(cols[i][j])+columnSpacing)
            rows[j]+=cols[i][j]
            if not i == len(headerRow)-1: rows[j]+=' '*columnSpacing

    line = '-'*len(header)
    print(line)
    print(header)
    print(line)
    for row in rows: print(row)
    print(line)
header = ['N','Brute Force', 'Binary Search', 'Hash Set', 'Sorting and Sweeping']
makeTable(header,[n,brute,binary, hash, sweep])
sys.stdout.close()
