nums = [3, 2, 2, 3]
val = 3


class Solution:
    def removeElement(nums, val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k, nums


print(Solution.removeElement(nums, val))
