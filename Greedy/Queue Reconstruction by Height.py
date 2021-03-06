# coding: utf-8
'''
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people
in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.
Note:
The number of people is less than 1,100.
Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

'''
首先选出k值为0且身高最低的人，记为hi, ki，将其加入结果集。

然后更新队列，若队列中人员的身高≤hi，则令其k值 - 1（需要记录原始的k值）。

循环直到队列为空。
'''


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people:
            return []
        peopledct, height, res = {}, [], []
        for i in xrange(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height += p[0],
        height.sort()
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])
        return res

solution = Solution()
print solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])