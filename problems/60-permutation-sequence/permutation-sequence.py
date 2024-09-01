import math
class Solution(object):
    def getPermutation(self, n, k):
        numbers=range(1,n+1) 
        permutation=''
        k=k-1
        while n>0:
            n=n-1
            index,k=divmod(k,math.factorial(n))
            permutation+=str(numbers[index])
            numbers.remove(numbers[index])
        return permutation
        

        
        