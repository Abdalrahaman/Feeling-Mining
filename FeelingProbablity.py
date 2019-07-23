def lineFileFormat(selectedFileWord):
    for indexWord in range(len(selectedFileWord)):
        selectedFileWord[indexWord] = selectedFileWord[indexWord].rstrip()
    return selectedFileWord


def getMaxProbablity(countList):
    maxValue = countList[0]
    maxIndexValue = 0
    for n in range(1, len(countList)):
        if countList[n] > maxValue:
            maxValue = countList[n]
            maxIndexValue = n

    if maxValue == 0:
        maxValue = -1
        maxIndexValue = -1
    return maxValue, maxIndexValue


class feelingProbablity:
    feelingCategories = ("السعاده", "الحزن", "الغضب", "الخوف", "القرف", "الدهشه")
    fileName = ("happy.txt", "sad.txt", "anger.txt", "fear.txt", "disgust.txt", "surprise.txt")

    def __init__(self, finalOutput):
        print("Feeling Selected is : ")
        self.finalOutput = finalOutput

    def probablityProcessing(self):
        # Search in feeling files
        countList = [0, 0, 0, 0, 0, 0]
        for indexSentence in range(len(self.finalOutput)):
            for indexSubSentence in range(len(self.finalOutput[indexSentence])):
                for indexFile in range(len(self.fileName)):
                    selectFileWord = open(self.fileName[indexFile], 'r', encoding='UTF-8')
                    print("from file : " + str(self.fileName[indexFile]) + " " + str(self.finalOutput[indexSentence][indexSubSentence][1]))
                    if self.finalOutput[indexSentence][indexSubSentence][1] in lineFileFormat(selectFileWord.readlines()):
                        countList[indexFile] += 1
                        break
        print(countList)
        # get feeling result
        feelingResult, feelingIndex = getMaxProbablity(countList)
        # check if not found feeling words
        if feelingResult != -1 and feelingIndex != -1:
            feeling = self.feelingCategories[feelingIndex]
        else:
            feeling = "لا شى !"
        return feeling, feelingIndex
