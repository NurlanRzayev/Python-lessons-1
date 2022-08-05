print('To stop input "stop"')

tags=set() #пустое множ. нельзя создать используя {} , так как тогда создается пустой словарь

phrase=''
while phrase!='stop':
    phrase=input()
    if phrase in tags:
        print('Tags have this phrase')
        continue #если условие выше выполнено нужно начать цикл сначала , на самом деле даже если этого не делать в tags не будет одинаковых phrase
    if phrase!='stop': #это условие было проверено в начале цикла , поэтому оно в любом случае вернет истину , оно эквивалентно if True
        tags.add(phrase)

print(tags)