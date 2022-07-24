"""
给定一个含有n个元素的数组，要求找到一个起始位置和一个结束位置，使这两个位置之间的元素之和最大
分治法
时间复杂度：T(n) = n*lg(n)
"""

import sys


def find_max_crossing_subarray(array, mid):
    '''
    查找横跨作用两部分的最大子数组，也就是第三种情况
    '''
    max_sum = -sys.maxsize - 1
    sum_now = 0
    i = mid
    left = i
    while i >= 0:  # 查找包含left_end的左边子数组
        sum_now += array[i]
        if sum_now > max_sum:
            left = i  # 记录下元素和最大时的元素下标
            max_sum = sum_now
        i -= 1
    left_max = max_sum
    j = mid + 1
    sum_now = 0
    right = j
    max_sum = -sys.maxsize - 1
    while j < len(array):  # 查找包含right_begin的右边子数组
        sum_now += array[j]
        if sum_now > max_sum:
            right = j
            max_sum = sum_now
        j += 1
    right_max = max_sum
    return array[left:right + 1], left_max + right_max


def find_max_subarray(array):
    if len(array) <= 1:
        return array, array[0]  # 当数组元素个数小于等于1时，直接返回
    left_part = array[0: int(len(array) / 2)]  # 将数组分割成两部分
    right_part = array[int(len(array) / 2):len(array)]
    left_sub_array, left_max = find_max_subarray(left_part)  # 递归求取左半部分最大子数组
    right_sub_array, right_max = find_max_subarray(right_part)  # 递归求取有半部分最大子数组
    crossing_sub_array, crossing_max = find_max_crossing_subarray(array, int(len(array) / 2) - 1)  # 获得横跨左右两部分的最大子数组
    max_sub_array, max_sum = left_sub_array, left_max
    if right_max > left_max:
        max_sub_array, max_sum = right_sub_array, right_max
    if crossing_max > max_sum:
        max_sub_array, max_sum = crossing_sub_array, crossing_max
    return max_sub_array, max_sum  # 三种情况中，元素和最大的数组就是整个数组的最大子数组


array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
sub_array, max_sum = find_max_subarray(array)
print("the max sub array is {0} and sum is: {1}".format(sub_array, max_sum))

"""
我自己的版本
"""

# class Solution:
#     def maxSubArray(self, nums) -> int:
#         if len(nums) == 1:
#             return nums[0]
#         mid = int(len(nums) / 2) - 1
#         right_part = nums[0:mid + 1]
#         left_part = nums[mid + 1::]
#
#         left_part_max = self.maxSubArray(left_part)
#         right_part_max = self.maxSubArray(right_part)
#         crossing_part_max = self.crossing_max(nums)
#         return max(left_part_max, right_part_max, crossing_part_max)
#
#     def crossing_max(self, array):
#         mid = int(len(array) / 2) - 1
#         left_end = mid
#         right_begin = mid + 1
#
#         left_sum = 0
#         left_max = array[left_end]
#         for i in array[left_end::-1]:
#             tem = left_sum + i
#             if tem > left_max:
#                 left_max = tem
#             left_sum = tem
#
#         right_sum = 0
#         right_max = array[right_begin]
#         for j in array[right_begin::]:
#             tem = right_sum + j
#             if tem > right_max:
#                 right_max = tem
#             right_sum = tem
#
#         return left_max + right_max
#
#
# solution = Solution()
# array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
# print(solution.maxSubArray(array))
