preference = input("Sisesta eelistus ('kuum' või 'külm'): ")

if preference == "kuum":
    type = input("Sisesta tüüp ('tee' või 'kohv'): ")
    if type == "tee":
        print("Valmistame teed")
    else:
        print("Valmistame kohvi")
else:
    print("Limonaad")
