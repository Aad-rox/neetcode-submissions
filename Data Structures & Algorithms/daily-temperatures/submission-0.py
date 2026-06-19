class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        tempStack=[]
        answer = [0]*len(temperatures)

        for i, temp in enumerate(temperatures):

            while len(tempStack) > 0 and temp > temperatures[tempStack[-1]]:

                day = tempStack.pop()
                answer[day] = i-day
            
            tempStack.append(i)

        return answer





         

            

            





        