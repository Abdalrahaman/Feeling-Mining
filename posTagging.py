import nltk


class posTagging():

    def __init__(self, tokenList):
        # self.Pos_tagg("محمد انسان ينصهر بشخصيته يعتز بالامل لعل هو يكن سعصصدا")
        print("PosTagging Output is")
        self.tokenList = tokenList

    def Pos_tagg(self):
        x = nltk.RegexpTagger(
            [('انا|نحن', 'ضمير منفصل متكلم'),
             ('أنتَ|أنتِ|أنتما|أنتم|أنتن', 'ضمائر المنفصلة للمخاطب'),
             ('هو|هي|هما|هنْ|هم', ' ضمائر المنفصلة للغائب '),
             ('أياي|ايانا|اياكِ|اياكما|اياكم|اياها|اياهما|اياهم|اياهن', 'ضمائر نصب'),
             ('الذي|التي|اللذان|اللتان|الذين|اللاتي', 'اسماء الوصل'),
             ('من|الى|حتى|خلا|حاشا|عدا|في|عن|على|مذ|منذ|رُب|كي|لعل|متى|لولا', 'حروف الجر'),
             (r'\bو\b'+'|'+r'\bلو\b', 'حرف عطف'),
             ('[ب|ك][ا-ى]+', 'ب/ك حرف جر متصل باسم'),
             ('ال[ا-ى]+', 'اسم'),
             ('[ا-ى]+را', 'مفعول لاجله'),
             ('[ا-ى]+دا', 'حال'),
             ('[انيت][ا-ى]+', 'فعل'),
             ('[ا-ى]+', 'اسم علم')
             ]
        )

        tagSentenceList = []
        for index in range(len(self.tokenList)):
            print(self.tokenList[index][1])
            tagWordList = x.tag([self.tokenList[index][0]])
            tagSentenceList.append(tagWordList[0][1])
        return tagSentenceList
