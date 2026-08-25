class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for string in strs:
            hashmap[tuple(sorted(string))].append(string)

        return [val for val in hashmap.values()]