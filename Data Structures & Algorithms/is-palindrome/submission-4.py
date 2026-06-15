class Solution:
    def isPalindrome(self, s: str) -> bool:

        stringList = s

        end = len(s)-1
        start = 0

        while start < end:
            if not stringList[start].isalnum():
                start+=1
                continue

            if not stringList[end].isalnum():
                end -=1
                continue
            
            if stringList[start].lower()!=stringList[end].lower():
                return False

            start+=1
            end-=1
        return True



       
       


        