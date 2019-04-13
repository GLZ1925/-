#coding:utf-8
import re

text = "“喂！路明非！你给我站住！”叔叔追了出来，在走廊尽头冲他低吼。路明非实在没时间让他兴师问罪了，只好说：“叔叔我真有事得先走，什么事以后再说！”叔叔可不听他说，跑过来一把抓住他的手：“你小子给我说老实话？是不是在外面惹事了？我看外面都是警车还有流氓，他们都是冲你来的？”“没……没有……”路明非想辩解。“你小子真不是骗我们说上学其实跑日本来混黑道了吧？”叔叔瞪着他。“真不是，这事儿一时没法解释……”叔叔从屁股后面摸出金利来的钱包，打开来夹层里有几张日圆钞票，大概一万多的样子。他把那张万圆大钞塞进路明非手里：“叔叔不知道你惹了什么麻烦，你们年轻人见的世面大，有些事不愿告诉我们大人，我问也没用。我以前也惹过事跑过路，跑路身上千万得有现金！银行卡信用卡跑车都没用！”"
def normal_cut_sentence(text):
    text = re.sub('([。！？\?])([^’”])',r'\1\n\2',text)#普通断句符号且后面没有引号
    text = re.sub('(\.{6})([^’”])',r'\1\n\2',text)#英文省略号且后面没有引号
    text = re.sub('(\…{2})([^’”])',r'\1\n\2',text)#中文省略号且后面没有引号
    text = re.sub('([.。！？\?\.{6}\…{2}][’”])([^’”])',r'\1\n\2',text)#断句号+引号且后面没有引号
    return text.split("\n")

def cut_sentence_with_quotation_marks(text):
    p = re.compile("“.*?”")
    list = []
    index = 0
    length = len(text)
    for i in p.finditer(text):
        temp = ''
        start = i.start()
        end = i.end()
        for j in range(index, start):
            temp += text[j]
        if temp != '':
            temp_list = normal_cut_sentence(temp)
            list += temp_list
        temp = ''
        for k in range(start, end):
            temp += text[k]
        if temp != ' ':
            list.append(temp)
        index = end
    return list

if __name__ == '__main__':
    print(cut_sentence_with_quotation_marks(text))