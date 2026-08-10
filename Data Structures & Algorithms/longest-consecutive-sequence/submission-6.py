class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for num in numbers:
            # Only begin at the start of a sequence,
            # so if there is no number before
            if num - 1 not in numbers:
                length = 1

                while num + length in numbers:
                    length += 1

                longest = max(longest, length)

        return longest