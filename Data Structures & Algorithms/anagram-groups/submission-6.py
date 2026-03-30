class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_bank = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for c in word:
                idx = ord(c) - ord('a')
                freq[idx] += 1
            word_bank[tuple(freq)].append(word)

        return list(word_bank.values())
