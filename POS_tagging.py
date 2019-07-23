
PRON = ['هي', 'هو', 'هن', 'هما', 'هم', 'انا', 'نحن', 'انت', 'انتما', 'انتم', 'انتن']  # ضمائر
DEM = ['هذا', 'هذه', 'هؤلاء', 'هاهنا', 'ذاك', 'ذلك', 'تلك', 'اولئك', 'هناك', 'هنالك']  # اسماء الاشاره
REL = ['الذي', 'التي', 'اللذان', 'اللتان', 'الذين', 'اللاتي']  # اسماء الوصل
VB = ['ي', 'ا', 'ن', 'س', 'سا', 'ت', 'است', 'أ']

proper_noun = open('Proper_noun.txt', 'r')
HROUF = open('HROUF.txt', 'r')

p_noun = []
for i in proper_noun:
    p_noun.append(i.strip())

hrouf = []
for i in HROUF:
    hrouf.append(i.strip())


def POS_Tag(list_tokens):
    dictionaray = {}
    for word in list_tokens:
        for verb in VB:
            if word.startswith(verb):
                dictionaray[word] = 'VERB'
                break
            else:
                dictionaray[word] = 'NOUN'
        for pron in PRON:
            if word == pron:
                dictionaray[word] = 'PRON'
                break
        for dem in DEM:
            if word == dem:
                dictionaray[word] = 'DEM'
                break
        if word.startswith('ال'):
            dictionaray[word] = 'NOUN'
        for rel in REL:
            if word == rel:
                dictionaray[word] = 'REL'
                break
        for p in p_noun:
            if word == p:
                dictionaray[word] = 'P_NOUN'
                break
        for hrf in hrouf:
            if word == hrf:
                dictionaray[word] = 'HRF'
                break

    return dictionaray

class POS_tagging:

    def __init__(self, list_tokens):
        self.list_tokens = list_tokens

    def pos_tagging(self):
        pos = POS_Tag(self.list_tokens)
        print("POS_tagging")
        return pos