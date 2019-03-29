def arrayPairSum(nums):
    """leetcode problem--561.Array Partition Ⅰ
    
    :param nums: List[int]
    :return: The minimum sum of each pair

    Example:
        Input: [1,4,3,2]
        Output: 4
        Explanation: n is 2, and the maximum sum of pairs is 4 = min(1,2) + min(3,4).
    """
    result = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        result += nums[i]
    return result

    # other solution
    # return sum(sorted(nums)[::2])

if __name__ == '__main__':
    test_list = [1,4,3,2]
    print(sorted(test_list)[::2])
    print(arrayPairSum(test_list))