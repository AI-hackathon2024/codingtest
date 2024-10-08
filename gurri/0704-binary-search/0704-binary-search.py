class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r :
            mid = (l + r) // 2
            
            # 1. target? 
            if nums[mid] == target : 
                return mid
            # lower bound ? 
            elif target < nums[mid] : 
                r = mid - 1
            # upper bound
            else : 
                l = mid + 1
        
        return -1