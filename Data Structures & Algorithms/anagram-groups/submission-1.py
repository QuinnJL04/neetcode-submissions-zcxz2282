class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_list = defaultdict(list)

        for word in strs:
            sorted_word = tuple(sorted(word))
            print(sorted_word)
            word_list[sorted_word].append(word)

        return list(word_list.values())
