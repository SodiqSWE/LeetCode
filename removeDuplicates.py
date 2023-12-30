# LeetCode problem: 26. Remove Duplicates from Sorted Array

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        left = 1

        for r in range(1, len(nums)):

            if nums[r] != nums[r - 1]:
                nums[left] = nums[r]
                left += 1

        return left
