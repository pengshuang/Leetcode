# coding: utf-8

'''
Given a string S and a string T,
count the number of distinct subsequences of T in S.

A subsequence of a string is a new string
which is formed from the original string
by deleting some (can be none) of the characters
without disturbing the relative positions of
the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s is None or t is None:
            return 0

        nums = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in xrange(0, len(s) + 1):
            nums[i][0] = 1
        for i in xrange(1, len(s)+1):
            for j in xrange(1, len(t)+1):
                nums[i][j] = nums[i-1][j]
                if s[i-1] == t[j-1]:
                    nums[i][j] += nums[i-1][j-1]

        return nums[len(s)][len(t)]

solution = Solution()
print solution.numDistinct("rabb", "rab")