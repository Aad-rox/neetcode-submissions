class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        leftProduct = 1

        rightProduct = 1


        leftarray = []

        for i in range(len(nums)):
            leftarray.append(leftProduct)
            leftProduct*=nums[i]



        for i in range(len(nums)-1, -1, -1):

            leftarray[i] *= rightProduct
            rightProduct*=nums[i]

        return leftarray




            

        
        