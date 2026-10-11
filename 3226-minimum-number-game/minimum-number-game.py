class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        rslt = []

        while len(nums) > 0:
            arr1 = min(nums)
            nums.remove(arr1)

            arr2 = min(nums)
            nums.remove(arr2)

            rslt.append(arr2)
            rslt.append(arr1)

        return rslt
