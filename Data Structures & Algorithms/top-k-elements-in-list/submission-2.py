class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output=[]
        dic={}
        for num in nums:
            dic[num] = nums.count(num)

        vals = sorted(dic.values())
        vals.reverse()

        for i in range(k):

            for key in dic.keys():

                if dic[key] == vals[i]:

                    if key not in output:

                        output.append(key)

        return output



        