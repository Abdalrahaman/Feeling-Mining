import re

patterns = [("فاعل", "\Dا\D{2}"),  # {2}[ا-ى]ا[ا-ى]
            ("مفعول", "م[ا-ى]{2}و[ا-ى]"),
            ("يفعل", "ي[ا-ى]{3}"),
            ("فعول", "[ا-ى]{2}و[ا-ى]"),
            ("فعيل", "[ا-ى]{2}ي[ا-ى]"),
            ("تفعيل", "ت[ا-ى]{2}ي[ا-ى]"),
            ("فعل", r'\b\D{3}\b')]


def prefixAndSuffixRemoval(wToken, prefixAR, suffixAR):
    wordToknize = list(map(lambda x: x + "", wToken))
    for index in range(len(wordToknize)):

        if not isPattern(wordToknize[index]):
            for suffix in suffixAR:
                if wordToknize[index][-len(suffix):] == suffix:
                    wordToknize[index] = wordToknize[index][:-len(suffix)]
                    break

        if not isPattern(wordToknize[index]):
            for prefix in prefixAR:
                if wordToknize[index][:len(prefix)] == prefix:
                    wordToknize[index] = wordToknize[index][len(prefix):]
                    break

    return wordToknize


def patternOperation(pattern, word):
    root = ""
    root += word[pattern.index("ف")]
    root += word[pattern.index("ع")]
    root += word[pattern.index("ل")]
    return root


def isPattern(affixWord):
    for pattern in patterns:
        if re.match(pattern[1], affixWord):
            return True
    return False


def patternGenerator(wordTokenize, affixesWord):
    rootList = []
    flag = False
    for index in range(len(affixesWord)):
        for pattern in patterns:
            if not affixesWord[index]:
                break
            if re.match(pattern[1], affixesWord[index]):
                rootList.append([wordTokenize[index], patternOperation(pattern[0], affixesWord[index])])
                flag = True
                break
        if not flag:
            rootList.append([wordTokenize[index], wordTokenize[index]])
        flag = False
    return rootList


class Stemming:
    prefixAR = ['ب', 'ك', 'س', 'و', 'ال', 'ا', 'ل', 'ف']
    suffixAR = ['ان', 'ون', 'ين', 'ات', 'وا', 'تم', 'هم', 'كم', 'ى', 'ه', 'ت', 'ك', 'ا', 'ن', 'و']

    def __init__(self, wordToknize):
        print("Stemming Output is : ")
        self.wordToknize = wordToknize

    def affixesRemoval(self):
        # print(prefixAndSuffixRemoval(self.wordToknize, self.prefixAR, self.suffixAR))
        stemList = prefixAndSuffixRemoval(self.wordToknize, self.prefixAR, self.suffixAR)
        # print(stemList)
        return stemList, patternGenerator(self.wordToknize, stemList)
