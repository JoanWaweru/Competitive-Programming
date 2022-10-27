class Solution(object):
    def sortSentence(self, s):
        shuffleArray = s.split(" ")
        finalSentence = ""
        for i in range(len(shuffleArray)):
            minimumIndex = i
            for j in range(i+1, len(shuffleArray)):
                if shuffleArray[j][-1] < shuffleArray[minimumIndex][-1]:
                    minimumIndex = j
            if i != minimumIndex:
                shuffleArray[minimumIndex], shuffleArray[i] = shuffleArray[i], shuffleArray[minimumIndex]
            finalSentence += shuffleArray[i][:-1] + ' '
        return (finalSentence[:-1])
        
       
        
        
