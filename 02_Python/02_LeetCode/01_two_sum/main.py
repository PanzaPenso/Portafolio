class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        result_list = []
        flag = True
        size_list = len(nums)
        i = 0
        while flag and i < size_list:
            current_num = nums[i]
            j = 0
            while j < size_list and flag:
                if j == i:
                    j += 1
                else:
                    total_sum = current_num + nums[j]
                    if total_sum == target:
                        result_list.append(i)
                        result_list.append(j)
                        flag = False
                    else:
                        j += 1
            i += 1

        return result_list

test = Solution()

print(test.twoSum([2,7,11,15], 18))