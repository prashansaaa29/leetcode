class Solution(object):
    def coinChange(self, coins, amount):
        p=[0]+([float('inf')]*amount)
        for i in range(1,amount+1):
            for j in coins:
                if j<=i:
                    p[i]=min(p[i],p[i-j]+1)
        if p[-1]==float('inf'):
            return -1
        return p[-1]