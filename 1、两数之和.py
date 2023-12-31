from typing import List

#List=[2,4,6,7]
class Solution:
    def twoSum(self,nums:List[int], target:int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]]

        return []

#  两数之和提交

# 我在dev 分支上了
# 新增 test 分支，试试