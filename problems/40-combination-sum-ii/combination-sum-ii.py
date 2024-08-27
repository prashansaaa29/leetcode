class Solution(object):
    def combinationSum2(self, candidates, target):
        res=[]
        
        def bfs(i,curr,total):
            if total==target:
                res.append(curr)
            if i==len(candidates) or total>target:
                return
            bfs(i+1,curr+[candidates[i]],total+candidates[i])
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i=i+1
            bfs(i+1,curr,total)
        bfs(0,[],0)
        d=[]
        for i in res:
            i.sort()
            if i not in d:
                d.append(i)
        return d
        