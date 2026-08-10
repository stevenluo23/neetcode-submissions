class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # build result in two passes: one for filling with prefix product, the other for suffix product
        # result: O(1) space
        pfxTotal = 1
        for i in range(n):
            res[i] = pfxTotal
            pfxTotal *= nums[i]

        sfxTotal = 1
        for i in range(n - 1, -1, -1):
            res[i] *= sfxTotal
            sfxTotal *= nums[i]
        
        return res