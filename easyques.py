import re
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs[0] == "":
            return ""
        for i in range(1, len(strs[0]) + 1):
            sub = strs[0][:i]
            check_list = list(map(lambda x: x[:i] == sub , strs))
            if False in check_list:
                return "" if i == 1 else out
            else:
                out = sub
    
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)
        return bin(sum)[2:]

    def mySqrt(self, x: int) -> int:
        for num in range(x//2+2):
            if num * num == x:
                return num
            if num * num > x:
                return num-1

    def removeElement(self, nums: List[int], val: int) -> int:
        nums = filter(val.__ne__, nums)
        return list(nums)

s = Solution()
sq = s.removeElement([3,2,2,3], 3)
print(sq)       
