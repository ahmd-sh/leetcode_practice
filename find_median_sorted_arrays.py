def findMedianSortedArrays():
    nums1 = [1,3]
    nums2 = [2]

    total = len(nums1) + len(nums2)
    half = total // 2

    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    l, r = 0, len(nums1)-1
    while True:
        mid = (l + r) // 2
        need_index = half - mid - 2

        left1 = nums1[mid] if mid >= 0 else float("-inf")
        right1 = nums1[mid+1] if (mid+1) < len(nums1) else float("inf")
        left2 = nums2[need_index] if need_index >= 0 else float("-inf")
        right2 = nums2[need_index+1] if (need_index+1) < len(nums2) else float("inf")

        if left1 <= right2 and right1 >= left2:
            if total % 2:
                return min(right1, right2)
            return (min(right1, right2) + max(left1, left2)) / 2

        elif left1 > right2:
            r = mid - 1

        else:
            l = mid + 1

print(findMedianSortedArrays())
