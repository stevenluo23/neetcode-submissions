class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # compute prefix and suffix separately, then create result
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # build prefix
        # core logic: prefix[i] = previous prefix product * previous number
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # build suffix
        # core logic: suffix[i] = forward suffix product * forward number
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        return [prefix[i] * suffix[i] for i in range(n)]