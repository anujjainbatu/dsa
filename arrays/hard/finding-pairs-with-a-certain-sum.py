# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

# v5.0 just with using python Counter()
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        new_value = old_value + val

        # update nums2
        self.nums2[index] = new_value

        # update freq2
        self.freq2[old_value] -= 1
        if self.freq2[old_value] == 0:
            del self.freq2[old_value]

        self.freq2[new_value] = self.freq2.get(new_value, 0) + 1

    def count(self, tot: int) -> int:
        count = 0

        for num1 in self.freq1:
            diff = tot - num1
            if diff in self.freq2:
                count += self.freq1[num1] * self.freq2[diff] 
                '''
                If:
                num1 appears 3 times in nums1
                diff appears 2 times in nums2
                3 × 2 = 6 valid pairs.
                '''
        return count

# v4.0 keeping frequency of both, count only has O(n) n = no. of unique element in nums1
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.freq1 = {}
        self.freq2 = {}

        for num in self.nums1:
            self.freq1[num] = self.freq1.get(num, 0) + 1

        for num in self.nums2:
            self.freq2[num] = self.freq2.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        old_value = self.nums2[index]
        new_value = old_value + val

        # update nums2
        self.nums2[index] = new_value

        # update freq2
        self.freq2[old_value] -= 1
        if self.freq2[old_value] == 0:
            del self.freq2[old_value]

        self.freq2[new_value] = self.freq2.get(new_value, 0) + 1

    def count(self, tot: int) -> int:
        count = 0

        for num1 in self.freq1:
            diff = tot - num1
            if diff in self.freq2:
                count += self.freq1[num1] * self.freq2[diff] 
                '''
                If:
                num1 appears 3 times in nums1
                diff appears 2 times in nums2
                3 × 2 = 6 valid pairs.
                '''
        return count

#v3.0 O(n+m) but freq1 is created only single time
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = {}

        for num in self.nums1:
            self.freq1[num] = self.freq1.get(num, 0) + 1

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        count = 0

        for num in self.nums2:
            diff = tot - num
            if diff in self.freq1:
                count += self.freq1[diff]
        
        return count

#v2.0 O(n+m) but make hash_map every time when count is called
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        n = len(self.nums1)
        m = len(self.nums2)
        hash_map = {}
        count = 0

        for num in self.nums1:
            hash_map[num] = hash_map.get(num, 0) + 1

        for num in self.nums2:
            diff = tot - num
            if diff in hash_map:
                count += hash_map[diff]
        
        return count

# v1.0 brute force O(n2)
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        n = len(self.nums1)
        m = len(self.nums2)
        count = 0

        for i in range(n):
            for j in range(m):
                if self.nums1[i] + self.nums2[j] == tot:
                    count += 1

        return count
                


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
