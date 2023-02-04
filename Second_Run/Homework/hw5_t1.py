#5.Напишите программу, удаляющую из текста все слова, содержащие "абв".

check =  'абв'
text1 = 'Проверочный текст один'
text2 = 'Проабверочный абвстрактный текст два абв'
#циклом
def cleanText(big:str,sub:str) -> str :
    temp = big.split()
    res = ''
    for word in temp:
        if sub in word:
            continue
        res +=word+' '
    return res[:-1]

#c "модными" функциями
def cleanText2(big:str,sub:str):
    temp = big.split()
    temp = list(filter(lambda w: sub not in w, temp))
    temp = ' '.join(temp)
    return temp
# print(cleanText(text1,check))
# print(cleanText(text2,check))
print(cleanText2(text1,check))
print(cleanText2(text2,check))
        