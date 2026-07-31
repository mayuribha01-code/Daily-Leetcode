class Solution:
    def minimumPushes(self, word: str) -> int:
        new=[]
        for i in word:
            if i not in new:
                new.append(i)
        m=[]
        for i in new:
            m.append(word.count(i))
        m=sorted(m)
        m=m[::-1]
        x=0
        for i in range (0,len(m)):
            if i<8:
                x+=(m[i])*(1)
            elif i<16:
                x+=(m[i]*2)
            elif i<24:
                x+=(m[i]*3)
            else:
                x+=(m[i]*4)
        return x