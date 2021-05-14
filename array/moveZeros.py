class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[nonZeroIndex] = nums[i]
                nonZeroIndex += 1
        for i in range(nonZeroIndex, len(nums)):
            nums[i] = 0
            