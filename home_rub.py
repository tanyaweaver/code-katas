def find_max_sum(nums):
    all_sums = []
    all_sums1 = helper_function(nums, 0, all_sums)
    all_sums2 = helper_function(nums[1:], 0, all_sums1)
    if len(all_sums2) != 0:
        return max(all_sums2)


def helper_function(nums, sum_so_far, all_sums):
    if not nums:
        all_sums.append(0)
        return all_sums
    if len(nums) < 3:
        all_sums.append(sum_so_far + nums[0])
        return all_sums
    else:
        new_sum_so_far = sum_so_far + nums[0]
        new_all_sums = helper_function(nums[2:], new_sum_so_far, all_sums)
        if len(nums) >= 4:
            return helper_function(nums[3:], new_sum_so_far, new_all_sums)
        return new_all_sums


if __name__ == '__main__':
    nums1 = [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6]
    nums3 = [122, 196, 128, 50, 61]
    nums2 = [230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79, 133, 66, 36, 165]
    nums = nums1 + nums3 + nums2
    #nums = [1, 2, 3, 4, 5]
    print find_max_sum(nums)
