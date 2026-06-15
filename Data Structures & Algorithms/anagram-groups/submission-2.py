class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = dict()

        for word in strs:
            if str(sorted(word)) not in dic.keys():
                dic[str(sorted(word))]=[]
                dic[str(sorted(word))].append(word)

            else:
                dic[str(sorted(word))].append(word)


        return list(dic.values())

                

            
                    


        