from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course, visited):

            if not course_map[course]: # No dependency
                return True
            
            if course in visited:
                return False
            
            visited.add(course)

            for p in course_map[course]:
                if not dfs(p, visited):
                    return False

            course_map[course] = []
            return True
        
        visited = set()
        course_map = defaultdict(list)
        for course, p in prerequisites:
            course_map[course].append(p)

        for course in range(numCourses):
            if not dfs(course, visited):
                return False
        
        return True