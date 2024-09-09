class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자기 자신 뺀 곱연산?
        ans = [1] * len(nums)
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        
        post = 1

        for i in range(len(nums)-1, -1, -1):
            ans[i] = post * ans[i]
            post *= nums[i]
        
        return ans