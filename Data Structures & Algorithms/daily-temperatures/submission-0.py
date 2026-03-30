class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        for i in range(len(temperatures)):
            count = 1
            print(f"i am counting {i} index")
            j = i+1
            while j < len(temperatures):
                if temperatures[j] > temperatures[i]:
                    break
                count+=1
                j+=1

            if j == len(temperatures):
                count = 0

            stack.append(count)
        
        return stack








