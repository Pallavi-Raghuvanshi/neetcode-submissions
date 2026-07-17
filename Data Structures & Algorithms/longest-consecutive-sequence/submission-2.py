class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        for num in list(nums):
            if num-1 not in nums:
                s = 1
                curr = num

                while curr + 1 in nums:
                    s += 1
                    curr += 1

                streak = max(streak,s)
        return streak