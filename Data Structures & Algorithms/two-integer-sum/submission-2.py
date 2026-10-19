class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store_prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in store_prev:
                return [store_prev[diff], i]
            store_prev[n] = i
            