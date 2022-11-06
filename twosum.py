class Solution():
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for n in nums:
            for i in nums:
                if n == i:
                    continue
                if n + i == target:
                    return [nums.index(n), nums.index(i)]


problem = Solution()

nums  = list(input())
target = int(input())
print(nums)

print(problem.twoSum(nums,target))
