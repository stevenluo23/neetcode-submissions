class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given a target and number x, find if y exists
        # return the pair of indices whose num sum = target

        n2i = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in n2i and n2i[complement] != i:
                return [n2i[complement], i]
            n2i[n] = i
        
        return []