class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tracker = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for c in word:
                arr[ord(c) - ord('a')] += 1
            tracker[tuple(arr)].append(word)

        return list(tracker.values())
