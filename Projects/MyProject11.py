""" FUNCTIONS """
# def salem_ber():
#     "Salem beriwshi funkciya"
#     print("Assalawma aleykum")
#
# salem_ber()

"""PARAMETRLI FUNKCIYALAR"""
# def salem_ber(name):
#     """PAYDALANIWSHI ATIN QABIL EIIP OPEN SALEM BEREDI"""
#     print(f"Assalawma aleykum hurmetli {name}")
# salem_ber("Ali")

"""FUNKCIYADAN BIR NESHE MARTE PAYDALANIW"""
# salem_ber('Hello')
# salem_ber("World")
# salem_ber("Aziz")

"""ARGUMENT HAM PARAMETR"""
# def salem_ber(name):
#     """Salem beriwshi funckiya"""
#     print(f"Salem {name.title()}")
# salem_ber("Ali")

"""FUNCKIYA BIR NESHE ARGUMENT UZAYTIW"""
# def full_name(name, name1):
#     """PAYDALANIWSHI MAGLIWMATLARIN JAMLEP
#     KONSOLGE SHIGARIWSHI FUNKCIYA"""
#     print(f"User name: {name.title()} \nUser last name: {name1.title()}")
# full_name("Aziz", "Sultanbek")
# full_name("Sanem", "Aziz")

# def age_calculator(name, birth):
#     """PAYDALANIWSHI JASIN ESAPLAWSHI FUNKCIYA"""
#     print(f"{name.title()}, {2023-birth} jasta")
# age_calculator('Aziz', 1998)
# age_calculator(1998, 'Zayfuna')
# age_calculator(birth=1998, name='Ali')

"""STANDART MANIS"""
# def age_calculator(birth, current_year=2022):
#     """PAYDALANIWSHI JASIN ESAPLAWSHI FUNKCIYA"""
#     print(f"{current_year-birth} jastasiz")
# age_calculator(2003)
# age_calculator(2003, 2023)

"""MANIS QAYTARIWSHI FUNKCIYALAR"""
# def full_name_generate(name, l_name):
#     """TOLIQ AT QAYTARIWSHI FUNCKIYA"""
#     full_name = f"{name} {l_name}"
#     return full_name
#
# full_name_1 = full_name_generate('Abiw', 'Aliev')
# full_name_2 = full_name_generate('Abiw', 'Sultan')
# print(f"Sabaqqa kelmegen studentler: {full_name_1} ham {full_name_2}")

"""QALEGEN ARGUMENT"""
# def genearte_full_name(name, l_name, f_name=" "):
#     """Toliq at qaytariwshi funkciya"""
#     if f_name:
#         full_name = f"{name} {f_name} {l_name}"
#     else:
#         full_name = f"{name} {l_name}"
#     return full_name
# student_1 = genearte_full_name('Aziz', 'Zayfuna')
# student_2 = genearte_full_name('Sultan', 'Amir')
# print(f" Sabaqqa kelmegen studentler: {student_1} ham {student_2}")

"""FUNCKIYADAN DICT QAYTARIW"""
# def avtomobil(kompaniya, model, ren, jil):
#     result = {
#         'company': kompaniya,
#         'model': model,
#         'color': ren,
#         'year': jil
#         }
#     return result
# avto_0 =  avtomobil("GM", "Malibu", "Qara", "2015")
# print(avto_0)
