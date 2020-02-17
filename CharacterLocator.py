def CharacterLocator(input,character):
    location=[]
    index=0
    for char in input:
        if char==character:
            location.append(index)
        index+=1
    return  location





print (CharacterLocator("This  is Javascript","i"))
