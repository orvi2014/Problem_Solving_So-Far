def sum67(nums):
       flag = True
       sum = 0
       for n in nums:
             if n == 6:
                 flag = False
             if flag:
                 sum += n
                 continue
             if n == 7:
                 flag = True
       return sum
