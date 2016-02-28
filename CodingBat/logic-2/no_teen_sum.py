def no_teen_sum(a, b, c):
     return fix_sum(a)+fix_sum(b)+fix_sum(c)
def fix_sum(n):
     if 13 <= n <= 14 or 17 <= n <= 19:
        return 0
     return n
  
