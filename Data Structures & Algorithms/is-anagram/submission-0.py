class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        word1_letters={}
        word2_letters={}

        for letter in s:
            if letter in word1_letters.keys():
                word1_letters[letter]+=1
            else:

                word1_letters[letter]=1


        for letter in t:
            if letter in word2_letters.keys():
                word2_letters[letter]+=1
            else:

                word2_letters[letter]=1


        return word1_letters == word2_letters

        

            
        