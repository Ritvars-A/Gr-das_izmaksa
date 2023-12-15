import math

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums):
    izmaksa = math.ceil(telpas_platums / linoleja_platums) * telpas_garums * cena

    return izmaksa
  
while True:
  try:
    cena1 = float(input("Linolejas cena EUR/m^2: "))
  except:
    print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")
  else:
    if cena1 > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")

while True:
  try:
    linoleja_platums1 = float(input("Linolejas platums metros: "))
  except: 
    print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")
  else:
    if linoleja_platums1 > 0:
      break
    else:
      print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")

while True: 
  try:
    platums1 = float(input("Grīdas platums metros: "))
  except:
    print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")
  else:
    if platums1 > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")

while True:
  try:
    garums1 = float(input("Grīdas garums metros: "))
  except: 
    print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")
  else:
    if garums1 > 0:
      break
    else: 
      print("Nepareizi ievadīta vērtība! Lūdzu ievadiet pozitīvu skaitli!")

print("Izklājot garumā:\n", gridas_izmaksa(cena1, linoleja_platums1, platums1, garums1))
print("Izklājot platumā:\n", gridas_izmaksa(cena1, linoleja_platums1, garums1, platums1))
