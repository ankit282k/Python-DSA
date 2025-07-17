class Solution:
    def check(nums: list[int]) -> bool:
        count = 0
        length = len(nums)
        for i in range(length):
            if nums[i]>nums[(i+1) % length]:
                count+=1

        if count>1:
            return False
        else:
            return True


if __name__ == '__main__':
    nums1 = [2, 1, 3, 4]
    nums2 = [3, 4, 5, 1, 2]
    result = Solution.check(nums2)
    print(result)