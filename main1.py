def matchwords(words):
    count=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
            lst.append(word)
    print(lst)
    return count


print(matchwords(["ABA","ABC","121"]))