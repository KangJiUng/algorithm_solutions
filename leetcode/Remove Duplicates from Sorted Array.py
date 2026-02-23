# After removing duplicates, return the number of unique elements k.


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pointer = 0

        for n in nums[1:]:
            if n != nums[pointer]:
                pointer += 1
                nums[pointer] = n

        cnt = pointer + 1
        return cnt
