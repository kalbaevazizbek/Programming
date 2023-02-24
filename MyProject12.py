"""OZGERTIRILIGEN FUNCKIYA (*args **kwargs)"""

"""*args USILI"""
# def summa(*sanlar):
#     """KIRGIZILGEN SANLARDIN QOSINDISIN ESAPLAYDI"""
#     result = 0
#     for san in sanlar:
#         result += san
#     return result
# print(summa(1,2,3,4,5))
# print(summa(12.8))
# print(summa(100, 200, 500))
#
# def summa(x, y, *sanlar):
#     """KIRGIZILGEN SANLARDIN QOSINDISIN ESAPLAYDI"""
#     return x + y + sum(sanlar)
# print(summa(12, 13, 1, 2, 3, 4))
# print(summa(2))

"""kwargs USILI"""
# def telefon_info(kompaniya, model, *magliwmatlar):
#     """TELEFON HAQQINDAGI MAGLIWMATTI  DICT KORINISINDE QAYTARIWSHI FUNKCIYA"""
#     magliwmatlar['kompaniya'] = kompaniya
#     magliwmatlar['model'] = model
#     return magliwmatlar
#
# telefon_1 = telefon_info('Samsung', 'S22', jil=2022, ren='qizil')
# telefon_2 = telefon_info('Apple', 'Iphone 12', jil=2022, ren='kok')
# print(telefon_1)
# print(telefon_2)

"""GLOBAL OZGERIWSHI"""
# def summa(x, y, *sanlar):
#     global a
#     a = 1
#     for san in sanlar:
#         a *= san
#     return a

"""IMPORT"""
# import ESAPLAR_SHIGARIW
# print(ESAPLAR_SHIGARIW.summa(1,2,3,4,5))

# from ESAPLAR_SHIGARIW import *
# print(summa(12,12,12))


