class Solution:
    def check(nums: list[int]) -> int:
        return len(nums)


if __name__ == '__main__':
    nums = [2, 1, 3, 4]
    result = Solution.check(nums)
    print(result)