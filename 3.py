candidates,target=[2,3,5],8
ans=[]
def find(candidates,target,comb):
    if target==0:
        ans.append(comb)
    if len(candidates)==0:
        return None
    find(candidates[:-1],target,comb)
    if target>=candidates[-1]:
        find(candidates,target-candidates[-1],comb+[candidates[-1]])
find(candidates,target,[])
print(ans)