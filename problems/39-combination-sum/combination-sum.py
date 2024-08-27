class Solution(object):
    def combinationSum(self, candidates, target):
        res=[]
        def dfs(i,curr,total):
            if total==target:
                res.append(curr[:])
                return
            if i==len(candidates) or total>target:
                return
            dfs(i,curr+[candidates[i]],total+candidates[i])
            dfs(i+1,curr,total)
        dfs(0,[],0)
        return res

