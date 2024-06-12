# def two_num_sum(nums, target):
#     """ 两数之和 """
#
#     # 方式1
#     for i in range(len(nums)):
#         result = target - nums[i]
#         if result not in nums or i == nums.index(result):
#             continue
#         else:
#             return [i, nums.index(result)]
#
#     # 方式2
#     # for i in range(len(nums) - 1):
#     #     for j in range(i + 1, len(nums)):
#     #         if target - nums[i] == nums[j]:
#     #             return [i, j]
#
#
# num = [3, 2, 4]
# target_num = 6
# print(two_num_sum(num, target_num))


def longest_consecutive(nums) -> int:
    """
    此函数用于求给定列表中的最长连续子串
    例如:
    输入：[9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6] 返回: 7  因为最大的连续字串为 [3,4,5,6,7,8,9]
    输入：[100, 4, 200, 1, 3, 2] 返回: 4  因为最大的连续字串为 [1,2,3,4]

    """

    # 方式一：先排除数据不合规的情况，再通过将数据排序，然后按照下标获取
    # 能实现此功能，但是事件复杂度大

    # if not nums:
    #     return 0
    #
    # nums = list(set(nums))
    # for i in range(len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] > nums[j]:
    #             nums[i], nums[j] = nums[j], nums[i]
    #
    # print("列表: \n", nums)
    # count = max_length = 1
    # for index in range(0, len(nums)):
    #     if nums[index] + 1 in nums:
    #         count += 1
    #         index = nums.index(nums[index] + 1)
    #     else:
    #         count = 1
    #     if count > max_length:
    #         max_length = count
    #
    # return max_length

    # 方式2：解题思路：从当前值的最小边界开始查找，即：n - 1 不在列表中存在时，每次如果n+1在列表中存在，则计数加1，然后n=n+1，再继续查找n+1直到不在列表中存在
    # tips: set的查找效率要比list高，所以下面将list转换为set
    if not nums:
        return 0

    num_set = set(nums)
    count = max_length = 1
    for num in num_set:
        if num - 1 not in num_set:
            while num + 1 in num_set:
                count += 1
                num += 1

            max_length = max(max_length, count)
            count = 1

    return max_length


# nums_list = [100, 4, 200, 1, 3, 2]
# nums_list = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
# nums_list = [1, 2, 0, 1]
nums_list = [1, 0, -1]


print(longest_consecutive(nums_list))
