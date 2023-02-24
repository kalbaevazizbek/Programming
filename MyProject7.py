"""TEMA: IF-ELSE OPERATORI"""
"""SALISTIRIW OPERATORLARI"""
# kishi   <
# kishi yamasa ten  <=
# ulken   >
# ulken yamasa ten   >=
# tenlik  ==
# tensizlik   !=
# and -- ham
# or -- yamasa


# if False:  # False - jalgan,  True - ras
#     print("Jur")


# age = 10
# if age == 18:           # Eger agenin manisi 18 ge ten bolsa
#     print("On segiz")   # Konsolga "On segiz" di shigar
# if age == 19:           # Eger agenin manisi 19 ga ten bolsa
#     print("On togiz")   # Konsolga "On togiz" di shigar
# if age == 20:           # Eger agenin manisi 20 ga ten bolsa
#     print("Jigirma")    # Konsolga "Jigirma" ni shigar
# else:                   # Yamasa (Keri jagdayda)
#     print("Aniqlanbagan...")  # Konsolge "Aniqlanbagan..." shigar


# age = 18
# if age == 18 and age == 19:
#     print("Orinlandi")
# else:
#     print("Orinlanbadi")


# ball = int(input(" ballin neshe "))
# if 60 <= ball <= 69:
#     print("3 lik")
# elif 70 <= ball <= 90:
#     print("4 lik")
# elif 90 <= ball <= 100:
#     print("5 lik")
# else:
#     print("Jigildin")


"""BOOLLEAN - True, False"""
# a = True # 1, 2
# b = False # 0
# print(True/2)

# cars = ["bmw", "gm", "mersedes", "ferrari"]
# if "bmw" in cars:
#     print("Bar")
# else:
#     print("Joq")


"""EKI LISTTI SALISTIRIW"""
# menu = ["palaw", "manti", "lavash", "narin"]
# zakazlar = ["shay", "manti", "palaw"]
# for i in zakazlar:
#     if i in menu:
#         print(f"{i} bizde bar")
#     else:
#         print(f"{i} bizde joq")


"""LISTTIN BOS EMES EKENIN TEKSERIW"""
# menu = ["palaw", "manti", "pelmen", "narin"]
# if menu:
#     print("Awqatlar bar")
# else:
#     print("Tawsildi")


# age = 18
# age_group = "Minor" if age < 18 else "Adult"
# print(age_group)


# age = 20
# if age < 18:
#     age_group = "Minor"
#     print(age_group)
# else:
#     age_group = "Adult"
#     print(age_group)