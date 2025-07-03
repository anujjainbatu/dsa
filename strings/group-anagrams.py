# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for string in strs:
            sorted_string = tuple(sorted(string))
            if sorted_string in hash_map:
                hash_map[sorted_string].append(string)
            else:
                hash_map[sorted_string] = [string]
        
        return list(hash_map.values())
