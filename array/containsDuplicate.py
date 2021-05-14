class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # for i in nums:
        #     if i in d:
        #         return True
        #     else:
        #         d[i] = 1
        # return False
        return len(nums) > len(set(nums))