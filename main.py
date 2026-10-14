from typing import List

def twoSum(nums:List[int],target:int)->List[int]:
    # YOUR ANSWER
    hash_map = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in hash_map: return [hash_map[need], i]
        hash_map[nums[i]] = i
    return []

# print(twoSum([2, 7, 11, 15], 9))