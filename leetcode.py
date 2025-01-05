class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapa = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mapa:
                print(i, mapa[diff])
            mapa[n] = i

Solution.twoSum(self = 1, nums= [2, 3, 5], target = 8)