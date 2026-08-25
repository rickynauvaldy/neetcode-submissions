class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)

        most_common = hashmap.most_common(k)

        return [val[0] for val in most_common]