def find_kth_largest(nums, k):
  k = len(nums) - k

  def quick_select(l, r):
      pivot, p = nums[r], l

      for i in range(l, r):
          if nums[i] <= pivot:
              nums[i], nums[p] = nums[p], nums[i]
              p += 1
      nums[p], nums[r] = nums[r], nums[p]
      
      if p < k:
          return quick_select(p + 1, r)
      elif p > k:
          return quick_select(l, p - 1)
      else:
          return nums[p]

  return quick_select(0, len(nums) - 1)
  
