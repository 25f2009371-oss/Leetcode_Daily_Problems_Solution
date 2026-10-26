class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        marr = []

        for i in nums1:
            marr.append(i)

        for j in nums2:
            marr.append(j)

        marr.sort()

        n = len(marr)

        if n % 2 != 0:
            return marr[n // 2]
        else:
            return (marr[n // 2 - 1] + marr[n // 2]) / 2