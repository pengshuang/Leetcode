# coding: utf-8
'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 1
        end = x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid * mid <= x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return int(end)
        return int(start)