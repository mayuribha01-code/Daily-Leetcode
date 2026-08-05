class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result=[]
        for i in matrix:
            sum=0
            for j in i:
                sum+=j
            result.append(sum)
        return result