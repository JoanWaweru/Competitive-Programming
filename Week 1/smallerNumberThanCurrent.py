class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedNumbers = sorted(nums)
        dictionary = {}
        result = []
        
        for i in range(len(sortedNumbers)):
            if sortedNumbers[i] not in dictionary:
                dictionary[sortedNumbers[i]] = i
                
        for i in nums:
            result.append(dictionary[i])
        return result
