"""this is my first time learning about dictionaries!

the practice problem on p99 says to store info about a person you know.
their first name, last name, age, and the city in which they live.
the keys should be first_name, last_name, age, and city.
then i need to print all their info stored in the dictionary.
since this is being uploaded to github i will use a fictional character to
avoid doxxing friends"""

nathanforu_0 = {'first_name':'nathan', 'last_name':'fielder', 'age':'39', 'city':'los angeles'}
print(nathanforu_0)
print(nathanforu_0['first_name'])
print(nathanforu_0['last_name'])
print(nathanforu_0['age'])
print(nathanforu_0['city'])
print(" \n")

"""problem on p105 says to make a dictionary containing 3 major rivers and the country
each river runs through. then use a loop to print the name of each river, the name of each country included in 
the dictionary, and a sentence about each river. 
Geography is not a strong-suit for me so instead of rivers and countries i will do my favorite couples from
pop culture. the woman as the river, the man as the country"""

fav_couples = {
    'april':'andy',
    'tris':'four',
    'katniss':'peeta',
}

for name1 in fav_couples.keys():
    print(name1)
print(" \n")
for name2 in fav_couples.values():
    print(name2)
print(" \n")
for name1,name2 in fav_couples.items():
   print(name1.title() + " goes with " + name2.title() + ".")



