
def sec_largest_num(nums: list[int])-> int:
        nums.sort()
        return nums[-2]


if __name__ == '__main__':
    arr = {2, 5, 1, 3, 0}
    arr2 = [1, 2, 4, 7, 7, 5]
    a = sec_largest_num(arr2)
    print(a)
