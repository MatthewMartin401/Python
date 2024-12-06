#My recursion and Memoize test.

#import functool.lru_cache

#Test recursive function.
def count(num):
    if num == 0: #Base case
        print(num)
        return
    print (num)
    count(num-1) #recursive case
    print(num)
    return #Base case

#Factorial Recursive Function.
def recursive_fact(factorial):
    if factorial <= 1: #Base Case
        return (factorial)
    else:
        return(factorial*recursive_fact(factorial-1)) #Recursive Case
    
#factorials are deterministic and have no side effects so they can be used with memoize.

#Factorial Memoize Recursive Function.
factorial_cache = {} #Dictionary
def recur_Base_fact_Memo(factorial): #Recursive Base Factorial Memoize.
    global factorial_cache
    if factorial <= 1:
        return (factorial) #Base Case
    if factorial in factorial_cache:
        print("Found")
        return factorial_cache[factorial]#Base case - Collects function and factorial from the cache, so it doesnt need to calculate it again.
    else:
        print("not found") #If its not in found in the cache, print "not found."
        factorial_cache[factorial] = (factorial*recur_Base_fact_Memo(factorial-1))#recursive case #Saves in Cache.
        return(factorial_cache[factorial]) #base case

count(5)

print(recursive_fact(9))

print(recur_Base_fact_Memo(9))  # Nothing Found
print(recur_Base_fact_Memo(9))  # Found
print(recur_Base_fact_Memo(5))  # Found
print(recur_Base_fact_Memo(11))  # Found and Nothing Found. 

