from stemming import *
from posTagging import *
from textProcessing import *
from FeelingProbablity import *
import nltk
import re


def addPosTagToFinalList(finalTagSentence, posTagSentence, indexSentence):
    for indexToken in range(len(finalTagSentence[indexSentence])):
        finalTagSentence[indexSentence][indexToken].append(posTagSentence[indexToken])


def main():
    global lemmaList
    finalTagSentence = []

    print("Welcome to FEELING MINING")
    # محمد يلعب الكره !,سيذهب الى المدرسه
    # ذهب محمد الى المدرسه حزين,ولكن رجع سعيد
    userInput = input("Enter a text : ")

    # list of sentence
    listOfSentence = re.split(",", userInput)
    print(listOfSentence)

    listOfToken = []
    listOfprocess = []

    # Tokenizer
    for sentence in listOfSentence:
        listOfToken.append(nltk.word_tokenize(sentence))
    print("list for each token")
    print(listOfToken)

    # text processing
    for sentenceToken in listOfToken:
        opTextProcess = TextProcessing(sentenceToken)
        listOfprocess.append(opTextProcess.textProcessing())
    print("three element")
    print(listOfprocess)

    # Stemming and lemmatization
    for sentenceProToken in listOfprocess:
        op1 = Stemming(sentenceProToken)
        affixesList, lemmaList = op1.affixesRemoval()
        finalTagSentence.append(lemmaList)
    print("Lemma is : " + str(finalTagSentence))

    # Pos Tagging
    for indexSentence in range(len(finalTagSentence)):
        op2 = posTagging(finalTagSentence[indexSentence])
        addPosTagToFinalList(finalTagSentence, op2.Pos_tagg(), indexSentence)
    print("Output final : " + str(finalTagSentence))

    ######################## Selected Feeling ###################################

    op3 = feelingProbablity(finalTagSentence)
    feelingOutput, feelingIndex = op3.probablityProcessing()
    print(feelingOutput)


if __name__ == '__main__':
    main()
