def sum13(nums):
       if len(nums) == 0:
           return 0

       for i in range(0, len(nums)):
              if nums[i] == 13:
                  nums[i] = 0
                  if i+1 < len(nums):
                      nums[i+1] = 0
       return sum(nums)
