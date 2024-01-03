# LeetCode problem: 1929. Concatenation of Array

nums = [1, 3, 2, 1]


class Solution:
    def getConcatenation(self, nums: [int]) -> [int]:
        length = len(nums)
        ans = []
        x = 0

        while x < 2:
            for i in range(length):
                ans.append(nums[i])

            x += 1

        return ans
