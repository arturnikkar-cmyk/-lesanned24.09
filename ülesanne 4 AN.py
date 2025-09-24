transport = input("Sisesta transport (buss või jalgsi): ")
weather = input("Sisesta ilm (vihm või päike): ")

if transport == "buss":
    if weather == "vihm":
        print("Söidame bussiga katu se all")
    else:
        print("Söidame bussiga mugavalt")
elif transport == "jalgsi":
    if weather == "vihm":
        print("Võtame vihmavarju")
    else:
        print("Läheme jalga")