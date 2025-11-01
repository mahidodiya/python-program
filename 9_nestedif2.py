'''
write program to rate match couple using zodic sign 

steps:
1.take zodic sign 
2.conditions
'''
sign1=input("Enter female zodic sign:")
sign2=input("Enter male zodic sign:")

if sign1.lower()=="aries":
    if sign2.lower() in ['aries','leo','sagittarius','gemini','libra','aquarius']:
        print("Perfect match")
    elif sign2.lower() in ['virgo','pisces']:
        print("partially match")
    else:
        print("no match")

elif sign1.lower()== "leo":
    if sign2.lower() in ['aries','leo','sagittarius','gemini','libra']:
        print("Perfect match")
    elif sign2.lower() in ['taurus','aquarius','cancer','scorpio','pisces']:
        print("Partially match")
    else:
        print("No match")
        
elif sign1.lower()== "sagittarius":
    if sign2.lower() in ['aries','leo','sagittarius','gemini','libra','aquarius']:
        print("Perfect match")
    elif sign2.lower() in ['cancer','scorpio','pisces']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "taurus":
    if sign2.lower() in ['taurus','virgo','capricorn','cancer','scorpio','pisces']:
        print("Perfect match")
    elif sign2.lower() in ['leo','libra']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "virgo":
    if sign2.lower() in ['taurus','virgo','capricorn','cancer','scorpio',]:
        print("Perfect match")
    elif sign2.lower() in ['leo','aquarius','pisces']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "capricorn":
    if sign2.lower() in ['taurus','virgo','capricorn','cancer','scorpio','pisces']:
        print("Perfect match")
    elif sign2.lower() in ['leo','libra']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "gemini":
    if sign2.lower() in ['aries','leo','gemini','libra','aquarius']:
        print("Perfect match")
    elif sign2.lower() in ['sagittarius','virgo','capricorn']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "libra":
    if sign2.lower() in ['leo','sagittarius','gemini','libra','aquarius']:
        print("Perfect match")
    elif sign2.lower() in ['virgo','capricorn','aries','taurus','pisces']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "aquarius":
    if sign2.lower() in ['aries','leo','sagittarius','gemini','libra','aquarius',]:
        print("Perfect match")
    elif sign2.lower() in ['pisces','scorpio']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "cancer":
    if sign2.lower() in ['taurus','virgo','capricorn','cancer','scorpio','pisces']:
        print("Perfect match")
    elif sign2.lower() in ['leo','sagittarius']:
        print("Partially match")
    else:
        print("No match")

elif sign1.lower()== "scorpio":
    if sign2.lower() in ['taurus','virgo','capricorn','cancer','scorpio','pisces']:
        print("Perfect match")
    elif sign2.lower() in ['leo','aries']:
        print("Partially match")
    else:
        print("No match")
        
elif sign1.lower()== "pisces":
    if sign2.lower() in ['taurus','capricorn','cancer','scorpio','pisces']:
        print("Perfect match")
    elif sign2.lower() in ['leo','aries','sagittarius','virgo']:
        print("Partially match")
    else:
        print("No match")
        
else:
    print("wrong zodic sign!!")
        

