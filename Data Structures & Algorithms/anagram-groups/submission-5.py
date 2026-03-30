class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for word in strs:
            check = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                check[idx] += 1
            seen[tuple(check)].append(word)

        res = []
        for li in seen.keys():
            res.append(seen[li])
        return res
        


