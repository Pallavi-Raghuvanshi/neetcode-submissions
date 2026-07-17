class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        streak = 0
        for i in list(nums):
            if i not in nums:
                continue
            s = 0
            if i-1 in nums:
                continue
            s = 1
            nums.remove(i)
            succ = i+1
            while succ in nums:
                s += 1
                nums.remove(succ)
                succ += 1
            streak = max(streak,s)
        return streak