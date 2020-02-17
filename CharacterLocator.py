def CharacterLocator(input,x):
    location=[]
    y=0
    for i in input:
        if i==x:
            location.append(y)
        y+=1
    return  location





print (CharacterLocator("This  is Javascript","i"))
