class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s=list(s)
        goal=list(goal)
        result= False
        count=0
        while count<len(s):
            if s==goal:
                result=True
            else:
                temp=s[0]
                for i in range (0,len(s)-1):
                    s[i]=s[i+1]
                s[len(s)-1]=temp
            count+=1
        return (result)

    