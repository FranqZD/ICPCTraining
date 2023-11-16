def findDifferentBinaryString(nums):
    
    Numeroapp = []
    s=""
    for i in range(len(nums[0])):
        Numeroapp.append("0")
    s="".join(Numeroapp)
    if s not in nums:
        return s  
    NumeroCopy=Numeroapp
    for i in range(len(s)):
        for l in range(len(s)):
            Numeroapp[l]="1"
            s="".join(Numeroapp)
            if s not in nums:
                return s
        Numeroapp=NumeroCopy
        
   # print(s)
    
nums = ["00","01"]
print(findDifferentBinaryString(nums))