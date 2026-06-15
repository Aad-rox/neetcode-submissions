class Solution        :
    def twoSum(self, nums: List[int], target: int) -> List[int]:


      map={}

      for i in range(len(nums)):

        num = nums[i]

        if (target-num) in map.keys():

            return [map[target-num],i]

        else:

            map[num]=i