# https://leetcode.com/problems/3sum/

'''
Complexity

* Time complexity: $O(n^2)$
* Space complexity: $O(1)$ (excluding result storage)
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            if i != 0 and nums[i-1] == nums[i]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return result

'''
Complexity

* Time complexity: $O(n^2 \cdot \log 3) = O(n^2)$ due to sorting 3-element lists
* Space complexity: $O(n^2)$ for the set of results
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = set()
        for i in range(n):
            my_set = set()
            for j in range(i + 1, n):
                c = -1 * (nums[i] + nums[j])
                if c in my_set:
                    temp = [nums[i], nums[j], c]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
        return [list(triplet) for triplet in result]

'''
Complexity

* Time complexity: $O(n^3)$
* Space complexity: $O(n^2)$
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        my_set = set()
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        my_set.add(triplet)
        return [list(ans) for ans in my_set]
