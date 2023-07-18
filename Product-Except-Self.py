def productExceptSelf(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import copy
        import math
        productsTBD = []

        currList = copy.deepcopy(nums)

        for i in range(len(nums)):
            currList.remove(nums[i])
            productsTBD.append(currList)
            currList = copy.deepcopy(nums)
        res = []
        for lists in productsTBD:
            res.append(math.prod(lists))
        return res


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))