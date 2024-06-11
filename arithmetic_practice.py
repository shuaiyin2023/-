num = [3, 2, 4]
target_num = 6


def two_num_sum(nums, target):
    """ 两数之和 """
    for i in range(len(nums)):
        result = target - nums[i]
        if result not in nums or i == nums.index(result):
            continue
        else:
            return [i, nums.index(result)]


print(two_num_sum(num, target_num))



