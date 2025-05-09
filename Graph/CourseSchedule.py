"""
Solution:
Runtime 47% O(V + E)
Memory 40% O(V + E)
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Intuition: Find a way to check if a course has a cycle. If it doesn't, memorize that.
            This will allow us to check once if coures are cyclic and re-use that computation when checking,
            other courses.
            On cycle: return False
            On full check without any cycles: return True

            -1 is cyclical
            0 is unchecked
            1 is acylic
        """
        adjList = {}
        for course, req in prerequisites:
            reqs = adjList.get(course, [])
            reqs.append(req)
            adjList[course] = reqs

        courseHasCycle = [0] * numCourses

        def hasCycle(course: int):
            if courseHasCycle[course] != 0:
                return courseHasCycle[course] == -1

            # mark as -1 to signal that taking this course again would cycle
            courseHasCycle[course] = -1

            for req in adjList.get(course, []):
                if hasCycle(req):
                    return True

            # mark as 1 to signal this course is acylic
            courseHasCycle[course] = 1

        for courseNumber in range(numCourses):
            if hasCycle(courseNumber):
                return False

        return True
