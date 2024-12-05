class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        
        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                prior_idx = stack.pop()
                output[prior_idx] = idx - prior_idx
            stack.append(idx)

        return output
