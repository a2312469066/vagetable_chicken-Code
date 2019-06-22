import itertools
VOWELS = "aeiouy"
def translate(phrase):
    alph_list = []
    for i in phrase:
        alph_list.append(i)
    #删除元音字母后的重复
    for index, alph_dic in itertools.groupby(alph_list,key=alph_list.index):
        a = len(list(alph_dic))
        if (a // 3) >= 1:
            for i in range(a // 3):
                alph_list.pop(index)
                alph_list.pop(index)
    print(alph_list)
    #删除辅音字母后的随机元音字母
    pop_index = []
    j = 0
    for i in alph_list:
        if i.isalpha():
            if VOWELS.find(i) == -1:

                pop_index.append(j+1)
            j+=1
    k = len(pop_index)
    i = 0
    while i < k:
        alph_list.pop(pop_index[i]-i)
        i += 1
    print(alph_list)



#        element_index = min(i,key=phrase.index)
#        index = phrase.find(element_index)
#        new_phrase = phrase[index:index+2]
#        print(new_phrase)
    return "".join(alph_list)

if __name__ == '__main__':
    print("Example:")
    print(translate("hoooowe yyyooouuu duoooiiine"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
