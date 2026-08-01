class Solution:
    def predictTheWinner( nums) -> bool:
        count=0
        count1=0
        count2=0
        f=[]
        if len(nums)==1:
            return True
        while len(nums)>3:
            a=0    
            b=len(nums)-1
            big=max(nums[a],nums[a+1],nums[b],nums[b-1])
            if big==nums[a] or big== nums[b]:
                count=big
            else:
                if big==nums[a+1]:
                    count=nums[b]
                else:
                    count=nums[a]
            nums.remove(count)
            f.append(count)
        if len(nums)<=3:
            nums=sorted(nums)
            nums= nums[::-1]
            f=f+nums
            print(f)
        for i in range (0, len(f)):
            if i%2==0:
                count2+=f[i]
        
            else:
                count1+=f[i]
        print(count2)
        print(count1)
        if count1>=count2:
            return True
        else:
            return False

    print(predictTheWinner([1,2]))