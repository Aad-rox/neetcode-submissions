class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = dict()
        l=[]

        for i in range(len(nums)):

            diff = target-nums[i]

            if diff in hm:
                l.append(hm[diff])
                l.append(i)
                return l
            hm[nums[i]] = i
                



        