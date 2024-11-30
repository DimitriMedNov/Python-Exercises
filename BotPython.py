from ctypes.wintypes import HLOCAL


bot = "thor"
print(bot + ": hola soy un bot perra")
def habla():
    tu = input("yo:")
    if "hola" in tu:
        print(bot + ": bien, que haces")
        habla()
    if "programando" in tu:
        print(bot + ": sabes mucho")
        habla()
    if "si" in tu:
        print(bot + ": que bueno")
        habla()
    else:
        print(bot + "chao")
habla()