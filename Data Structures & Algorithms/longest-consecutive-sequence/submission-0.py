class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq = 0
        for i in range(len(nums)):
            cur_set = set()
            cur_set.add(nums[i])
            added = True
            while added:
                added = False
                for j in range(len(nums)):
                    if nums[j] not in cur_set and nums[j] == max(cur_set) + 1 or nums[j] == min(cur_set) - 1:
                        cur_set.add(nums[j])
                        added = True
                print(cur_set)
            longest_seq = max(len(cur_set), longest_seq)
        return longest_seq