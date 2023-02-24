"""TEMA: LISTLER"""
# fruits = ['alma', 'almurt', 'shiyshe', 'erik']      # string
# prices = [12000, 18000, 19000, 22100]               # integer
# numbers = ["bir", "eki", "3", '4', "5"]             # aralas list
# names = []                                          # bos list
# print(names)

# 1)
# names = ["Atabek", "Sanemxan", "Samandar"]
# print(f"Qalay {names[0]} aman saw densawligin jaqsima")
# 2)
# t_shaxs = ["Al-Farabiy", "Al-Xorezmiy", "Al-Beruniy"]
# z_shaxs = ["Allambergen", "Fayzulla", "Buxarbay"]
# print(f"Men tariyxiy shaxslardan {t_shaxs.pop()} menen \nhazirgi tiri shaxslardan {z_shaxs.pop(2)} hurmet qilaman")
# 3)
# friends = []
# friends.append("Sanemxan")
# friends.append("Zayfuna")
# friends.append("Atabek")
# print(" Menin dostim ", friends)
# 4)
# friends = ["Atabek", "Samandar", "Shuxrat", "Zayfuna", "Azizbek"]
# friends.remove("Zayfuna")
# print(f"Otirispaqqa {friends} kele almaydi")
# 5)
# friends = ["Atabek", "Samandar", "Shuxrat", "Zayfuna", "Azizbek"]
# taza_miymanlar = ["Gulzar", "Venera", "Guljayna", "Yulduz"]
# taza_miymanlar.append(friends.pop(0))
# taza_miymanlar.append(friends.pop(1))
# taza_miymanlar.append(friends.pop(2))
# print(friends, "\n", taza_miymanlar)

"""LISTTEN MENEN ISLEW"""
"""Listtlerdi tartiplew"""
# cars = ["Bugatti", "Mersedes", "Bmw", "Ferari", "Lamborghini"]
# cars.sort()
# print(cars)

# listtegi elementlerdin qaysi bas harippen jazilgan bolsa sol 0 linshi element boladi
# cars = ["Bugatti", "Mersedes", "Bmw", "Ferari", "Lamborghini"]
# cars.sort(reverse=True)
# print(cars)
"""SORT() METODI LIST ELEMNETLERIN TAQLAW"""
# ages = [7, 19, 30, 55, 78]
# ages.sort() # LIST ELEMENTLERIN TAQLAW
# print(ages)
# print(sorted(ages, reverse=True))
# cars = ["Bugatti", "Mersedes", "Bmw", "Ferari", "Lamborghini"]
# cars.reverse()
# print(cars)

"""LEN() FUNCKCIYASI"""
# cars = ["Bugatti", "Mersedes", "Bmw", "Ferari", "Lamborghini"]
# print("Elementler sani", len(cars)) # LIST ELEMENTLERI SANI
"""RANGE() FUNKCIYASI"""
# sanlar = list(range(0,10))
# print(sanlar)

"""SANLI LISTLER MENEN ISLEW"""
# prices = [200, 300, 400, 500, 600, 1200]
# arzan = min(prices)
# qimbat = max(prices)
# jami = sum(prices)
# print("En arzan baxa", arzan, "En qimbat baha", qimbat, "Jami baxa", jami)


"""LIST USHIN METODLAR (PEREVODI)"""
# append()   ----  listtin aqirina element qosiw
# insert()   ____  qalegen indeksge element qosiw
# pop()      ----  elementti suwirip aliw
# del        ----  indeks yamasa osgeriwshi ati arqali oshiriw
# remove()   ____  element manisi oshiriw
# reverse()  ____  listti aylandiriw
# sorted()   ----  bir martelik sortlaw
