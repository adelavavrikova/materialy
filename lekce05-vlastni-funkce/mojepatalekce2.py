# do tech zavorek davam veci, co rozhodujou
#def cena_mhd(vek):
 #   print("Pocitam cenu lístku pro věk", vek)
 #   if vek < 6:
 #       print("Cena 0.")
  #  elif vek < 18:
  #      print("Cena 39.")
  #  elif vek < 65:
  #      print("Cena 50.")
  #  else:
  #      print("Jsi starý, máš to za fre.")

# cena_mhd(27)

# tedka chci ulozit, kolik mam strhnout z uctu, kdyz si tu jizdenku nekdo koupi
# zustatek_uctu = zustatek_uctu - cena_jizdenky 
# stejne jako input, ale muze i funkce vracet hodnotu, treba kolik ma stat jizdne
# uz nepotrebuju aby mi ta funkce vypsala ten vek, chci jen, aby mi vratila ty hodnoty

def cena_mhd(vek):
    if vek < 6:
        return 0 
    elif vek < 18:
        return 39
    elif vek < 65:
        return 50
    else:
        return 0

zustatek_uctu = 100
cena_jizdenky = cena_mhd(27)
zustatek_uctu = zustatek_uctu - cena_jizdenky
print("Vyslena cena je", cena_jizdenky, "na uctu zbyva:", zustatek_uctu)
