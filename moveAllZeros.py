nums = [0,1,0,3,12]
i=0
j=0
for x in range (0,len(nums)):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        print(i)
    j+=1
print(nums)
