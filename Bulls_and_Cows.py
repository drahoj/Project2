import random

def vytvor_nahodne_cislo() -> list:
  """ fce vytvori nahodne cislo"""
  konecne = True
  while konecne:
    cislo = str(random.randrange(1000,9999))
    cislo = set(cislo)
    cislo = list(cislo)
    if len(cislo) == 4 and cislo[0] != '0':
      konecne = False
  return cislo


def uvitani() -> str:
  """ funkce pozdravi a vypise uvodni text"""
  print('Hi there!')
  uvod = "I've generated a random 4 digit number for you."
  delka = len(uvod)
  print('-' * delka)
  print(uvod)
  print("Let's play a bulls and cows game.")
  print('-' * delka)
  print('Enter a number:')
  print('-' * delka)
  return delka


def je_cislo(cislo) -> bool:
  """ funkce jistuje, zda uzivatel zadal cislo"""
  try:
    cislo = int(cislo)
  except ValueError:
    print("You must enter number not a letter!")
    return False
  return True


def osetreni_cisla(h_cislo) -> bool:
  """ funkce zjistuje, zda zadana cisla:
        - jsou 4 mistna
        - cisla neobsahuji duplicity
        - cislo nezacina nulou"""
  if len(h_cislo) == 4:
    if len(set(h_cislo)) != 4:
      print('You must fill in unique 4 numbers!')
      return False
    if int(h_cislo[0]) == 0:
      print('You must fill in number that not begins with 0!')
      return False
    return True
  else:
    print('You must fill in 4 numbers!')
    return False


def jsou_cisla(h_cislo,n_cislo) -> dict:
  """ funkce zjistuje, zda jsou zadana cisla mezi hadanymi a prirazuje hodnoty
      bulls a cows"""
  bulls = 0
  cows = 0
  vysl = {'bulls' : 0,'cows' : 0}
  for i,cislo in enumerate(n_cislo):
    for j in range(len(n_cislo)):
      if h_cislo[j] == cislo:
        if j == i: #cislo je na spravne pozici
          bulls += 1
        else:
          cows += 1
  vysl['bulls'] = vysl['bulls'] + bulls
  vysl['cows'] = vysl['cows'] + cows
  return vysl


def main() -> None:
  delka_radku = uvitani()
  nahodne_cislo = vytvor_nahodne_cislo()
  konec_hry = True
  vysledek = {'bulls' : 0,'cows' : 0}
  pocet = 0
  while konec_hry:
    hadane_cislo = input()
    jedna_se_o_cislo = je_cislo(hadane_cislo)
    if jedna_se_o_cislo:
      if osetreni_cisla(hadane_cislo):
        pocet += 1
        vysledek = jsou_cisla(hadane_cislo,nahodne_cislo)
        if vysledek['bulls'] == 4:
          print("Correct, you've guessed the right number")
          print(f"in {pocet} guesses!")
          print('-' * delka_radku)
          konec_hry = False
        else:
          if vysledek['bulls'] == 1 and vysledek['cows'] == 1:
            print(f"{vysledek['bulls']} bull, {vysledek['cows']} cow")
          elif vysledek['bulls'] == 1 and vysledek['cows'] != 1:
            print(f"{vysledek['bulls']} bull, {vysledek['cows']} cows")
          elif vysledek['bulls'] != 1 and vysledek['cows'] == 1:
            print(f"{vysledek['bulls']} bulls, {vysledek['cows']} cow")
          else:
            print(f"{vysledek['bulls']} bulls, {vysledek['cows']} cows")
          print('-' * delka_radku)
   

main()