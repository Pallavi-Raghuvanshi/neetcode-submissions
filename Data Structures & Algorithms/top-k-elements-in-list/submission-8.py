class Solution:
    def topKFrequent(self, nums, k):
        # 1. Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # 2. Get unique frequencies in descending order
        unique_freqs = sorted(set(freq.values()), reverse=True)  # highest first

        result = []
        for f in unique_freqs:
            # Find all numbers with this frequency
            candidates = [num for num, count in freq.items() if count == f]
            # Add as many as needed to reach k
            needed = k - len(result)
            result.extend(candidates[:needed])
            if len(result) == k:
                break

        return result