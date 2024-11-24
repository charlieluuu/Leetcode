class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = m - 1, n - 1, m + n - 1

        # Compare elements from the end of nums1 and nums2
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # Copy remaining elements from nums2 if any
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

if __name__ == '__main__':
    solution = Solution()
    result = solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    print(result)