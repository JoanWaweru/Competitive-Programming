class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        q = collections.deque(nums)

        
        result = []
        while len(q) > 0:
            if len(q) > 0:
                result.append(q.popleft())
            if len(q) > 0:
                result.append(q.pop())
        return result
