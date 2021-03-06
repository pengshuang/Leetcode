# coding: utf-8

'''
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.
Subscribe to see which companies asked this question
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        str = ""
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while num != 0:
            while num >= value[i]:
                num -= value[i]
                str += symbol[i]
            i += 1
        return str

solution = Solution()
print solution.intToRoman(6)