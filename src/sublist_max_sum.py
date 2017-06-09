def sublist_max_sum(arr):
    """
    Find the biggest sum that can be calculated on a contiguous subarray.
    len(subarray) >= 1
    """
    if not arr:
        return
    max_sum, cur_sum = 0, 0
    for x in arr:
        cur_sum += x
        if cur_sum < 0:
            cur_sum = 0
        max_sum = max(max_sum, cur_sum)
    if max_sum == 0 and 0 not in arr:
        max_sum = max(arr)
    return max_sum
