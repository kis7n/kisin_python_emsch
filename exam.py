class Solution:
    def convert(self, s: str, numRows: int) -> str:
        x=[""]*numRows
        j=0
        b=len(x)
        while j<len(s):
            for i in range(0,b):
                if j<len(s):
                    x[i]+=s[j]
                    j+=1
                else:
                    break
            for i in range(b-2,0,-1):
                if j<len(s):
                    x[i]+=s[j]
                    j+=1
                else:
                    break
        return "".join(x)