class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        words = sentence.split()
        for element in dict:
            count = 0
            for str in words:
                if str.startswith(element):
                    words[count] = element
                count += 1
        sentence = words[0]
        for i in range(1,len(words)):
            sentence += ' '+words[i]
        print(sentence)
        return sentence

sol = Solution()
sol.replaceWords(["cat", "bat", "rat"],
"the cattle was rattled by the battery")