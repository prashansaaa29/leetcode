import math
class Solution(object):
    def getPermutation(self, n, k):
        numbers=range(1,n+1)
        p=''
        k=k-1
        while n>0:
            n=n-1
            i,k=divmod(k,math.factorial(n))
            p=p+str(numbers[i])
            numbers.remove(numbers[i])
        return p
        

        
        