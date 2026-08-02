height = [1,8,6,2,5,4,8,3,7]
a=0
b=len(height)-1
maxarea=0
while a<b:
    area=(min(height[a],height[b]))*(b-a)
    print(a,b)
    print(area)
    if area>maxarea:
        maxarea=area
    if height[a]<height[b]:
        a+=1
    else:
        b-=1
print(maxarea)