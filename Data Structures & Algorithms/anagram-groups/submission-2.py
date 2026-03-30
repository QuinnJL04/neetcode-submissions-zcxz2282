class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_list = defaultdict(list)

        for word in strs:
            letter_index = [0] * 26
            for c in word:
                letter_index[ord(c) - ord('a')] += 1
            word_list[tuple(letter_index)].append(word)
        return list(word_list.values())
