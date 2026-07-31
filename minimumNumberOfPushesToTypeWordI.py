class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)//8
        result=0
        for i in range (1,n+1):
            result +=(i*8)
        j=len(word)%8
        result+=(j*(n+1))
        
        return result 
        