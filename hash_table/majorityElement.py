class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = int(len(nums)/2)
        seen = {}
        
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
                
        for k, v in seen.items():
            if v > m:
                return k