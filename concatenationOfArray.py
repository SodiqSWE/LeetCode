# LeetCode problem: 1929. Concatenation of Array

nums = [1, 3, 2, 1]


class Solution:
    def getConcatenation(self, nums: [int]) -> [int]:
        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)

        return ans
