from datetime import datetime


def find_max_sum(nums):
    all_sums = []
    index_hash = {}
    all_sums1, index_hash1 = helper_function(0, 0, all_sums, index_hash)
    all_sums2, index_hash2 = helper_function(1, 0, all_sums1, index_hash1)
    if len(all_sums2) != 0:
        return max(all_sums2)


def helper_function(index, sum_so_far, all_sums, index_hash):
    if not nums[index:]:
        all_sums.append(0)
        return all_sums, index_hash
    if len(nums[index:]) < 3:
        all_sums.append(sum_so_far + nums[index])
        return all_sums, index_hash
    else:
        new_sum_so_far = sum_so_far + nums[index]
        if index in index_hash and new_sum_so_far <= index_hash[index]:
                return all_sums, index_hash
        else:
            index_hash[index] = new_sum_so_far
            new_all_sums, new_index_hash = helper_function(index + 2, new_sum_so_far, all_sums, index_hash)
            if len(nums[index:]) >= 4:
                new_all_sums1, new_index_hash1 = helper_function(index + 3, new_sum_so_far, new_all_sums, new_index_hash)
                return new_all_sums1, new_index_hash1
            return new_all_sums, new_index_hash


def robbery_clever(nums):
    a = b = 0
    for x in nums:
        a, b = b + x, max(a, b)
        return max(a, b)


if __name__ == '__main__':
    nums1 = [155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55, 6]
    nums3 = [122, 196, 128, 50, 61]
    nums2 = [230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241, 242, 157, 79, 133, 66, 36, 165]
    nums = nums1 + nums3 + nums2
    #nums = [1, 2, 3, 4, 5]
    t1 = datetime.now()
    print find_max_sum(nums)
    print 'time took: ', datetime.now() - t1
