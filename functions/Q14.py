def vowel_count(word):
    count=0
    store= word.lower()
    print(store)
    for i in store:
        if(i== 'a'or i == 'e' or i == 'i' or i=='o' or i=='u' ):
            count=count+1
    print(count)

vowel_count("appLe")    

