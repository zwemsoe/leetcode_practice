class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n+1)/2
        return int(expected - sum(nums))