'''
write a program to accept birth day and birth month from user. decide zodiac sign from below table 
    Aries: March 21–April 19
    Taurus: April 20–May 20
    Gemini: May 21–June 21
    Cancer: June 22–July 22
    Leo: July 23–August 22
    Virgo: August 23–September 22
    Libra: September 23–October 22
    Scorpio: October 24–November 21
    Sagittarius: November 22–December 21
    Capricorn: December 22–January 19
    Aquarius: January 20–February 18
    Pisces: February 19–March 20
    
    steps:
    1.enter birth day
    2.enter birth month
    3.check conditions
'''
day=int(input("Enter birth day:"))
month=input("Enter birth month:")

if (month.lower()=="march" and day>=21) or (month=="april" and day<=19):
    print("Zodic sign is aries")
elif  (month.lower()=="april" and day>=20) or (month=="may" and day<=20):
    print("Zodic sign is Taurus")
elif  (month.lower()=="may" and day>=21) or (month=="june" and day<=21):
    print("Zodic sign is Gemini")
elif  (month.lower()=="june" and day>=22) or (month=="july" and day<=22):
    print("Zodic sign is Cancer")
elif  (month.lower()=="july" and day>=23) or (month=="august" and day<=22):
    print("Zodic sign is Leo")
elif  (month.lower()=="august" and day>=23) or (month=="september" and day<=22):
    print("Zodic sign is Virgo")
elif  (month.lower()=="september" and day>=23) or (month=="october" and day<=22):
    print("Zodic sign is Libra")
elif  (month.lower()=="october" and day>=23) or (month=="november" and day<=24):
    print("Zodic sign is Scorpio")
elif  (month.lower()=="november" and day>=22) or (month=="december" and day<=21):
    print("Zodic sign is Sagittarius")
elif  (month.lower()=="december" and day>=22) or (month=="january" and day<=19):
    print("Zodic sign is Capricorn")
elif  (month.lower()=="january" and day>=20) or (month=="february" and day<=18):
    print("Zodic sign is Aquarius")
else: 
    print("Zodic sign is Pisces")
   
    
 