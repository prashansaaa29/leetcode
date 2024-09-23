class Solution(object):
    def reverseWords(self, s):
        a=s.split(" ")
        b=[]
        for i in a:
            if i!="":
                b.append(i)
        r=b[::-1]
        return ' '.join(r)
            




        """
        :type s: str
        :rtype: str
        """
        