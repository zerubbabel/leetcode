nums=[10,5,2,6]
k=100
n=len(nums)
val=1
ans=0
i,j=0,0
while j<n:
    while j<n and val*nums[j]<k:
        ans+=1
        val*=nums[j]
        j+=1
    while val>k and i<j:
        val//=nums[i]
        i+=1

print(ans)