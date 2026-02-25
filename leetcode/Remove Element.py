class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        pointer = 0

        for n in nums:
            if n != val:
                nums[pointer] = n
                pointer += 1

        return pointer
