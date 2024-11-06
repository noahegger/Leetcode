class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        # recursive function to build string of ()s
        def backtrack(curr, open_count, close_count):
            print(curr, open_count, close_count)
            if len(curr) == 2*n:
                result.append(curr)
                return
            
            if open_count < n:
                backtrack(curr+ "(", open_count+1, close_count)
            
            if close_count < open_count:
                backtrack(curr+ ")", open_count, close_count+1)
        
        backtrack("", 0, 0)
        return result