prices =  [7,1,5,3,6,4]
maxRe=0
for i in range (0,len(prices)):
    for j in range (i+1, len(prices)):
        if i==j:
            continue
        else:
            total=prices[j]-prices[i]
            if total>maxRe:
                maxRe=total
print(maxRe)

        