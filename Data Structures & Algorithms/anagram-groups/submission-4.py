class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        library = defaultdict(list)

        for word in strs:
            key = [0] * 26
            for c in word:
                key[ord(c) - ord('a')] += 1
            library[tuple(key)].append(word)
        
        return library.values()

