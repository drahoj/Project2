def uvod(delka_textu) -> dict:
  """ fukce vypise uvodni text. Vraci slovnik, ve kterem je ulozena hodnota delky
      textu (z duvodu centrovani textu - nenasel jsem jiny zpusob, jak udelat)"""
  print('Welcome to Tic Tac Toe')
  print('=' * delka_textu)
  xx = {'delka_textu':delka_textu}
  print('{:^{delka_textu}}'.format('GAME RULES:',**xx))
  print("Each player can place one mark (or stone)")
  print('per turn on the 3x3 grid. The WINNER is')
  print('who succeeds in placing three of their')
  print('marks in a:')
  print('* horizontal,')
  print('* vertical or')
  print('* diagonal row')
  print('=' * delka_textu)
  print('{:^{delka_textu}}'.format("Let's start the game",**xx))
  print('-' * delka_textu)
  return xx


def tisk_hraci_kostky(data,pozice) -> None:
  """ funkce vykresli hraci kostku"""
  for row in data:
    print('{:>{tabulator}} {:^{delka_znaku}} {:<{tabulator}}'.format(*row,**pozice))


def centrovani_textu(delka_textu,delka_znaku) -> dict:
  """ funkce spocita, kolik znaku musi byt pred a za znaky matice, aby byla matice ve stredu."""
  if delka_textu % 2 != 0:
    delka_textu += 1
  if delka_znaku % 2 != 0:
    delka_znaku -= 1
  tabulator = int((delka_textu - delka_znaku -3)/2)
  vystup = {'tabulator': tabulator,'delka_znaku' : delka_znaku}
  return vystup

  
def je_cislo(cislo) -> bool:
  """ funkce zjisti, zda zadana hodnota je cislo. V pripade, ze neni, informuje hrace,
      aby zadal cislo a ne pismeno"""
  try:
    cislo = int(cislo)
  except ValueError:
    print("You must enter number not a letter!")
    return False
  return True


def osetreni_cisla(cislo) -> bool:
  """ funkce zyjistim, zda hrac zadal cisla mezi 1 a 9. Pokud ne, upozorni ho"""
  if cislo in range(1,10):
    return True
  else:
    print('You must fill in number between 1 to 9')
    return False


def konec_hry(kameny,jaky_hrac) -> bool:
  """ funkce zjistuje, zda jeden z hracu neumistil kameny do viteyne polohy"""
  if kameny[0] == jaky_hrac and kameny[1] == jaky_hrac and kameny[2] == jaky_hrac:
    return False
  elif kameny[3] == jaky_hrac and kameny[4] == jaky_hrac and kameny[5] == jaky_hrac:
    return False
  elif kameny[6] == jaky_hrac and kameny[7] == jaky_hrac and kameny[8] == jaky_hrac:
    return False
  elif kameny[0] == jaky_hrac and kameny[3] == jaky_hrac and kameny[6] == jaky_hrac:
    return False
  elif kameny[1] == jaky_hrac and kameny[4] == jaky_hrac and kameny[7] == jaky_hrac:
    return False
  elif kameny[2] == jaky_hrac and kameny[5] == jaky_hrac and kameny[8] == jaky_hrac:
    return False
  elif kameny[0] == jaky_hrac and kameny[4] == jaky_hrac and kameny[8] == jaky_hrac:
    return False
  elif kameny[2] == jaky_hrac and kameny[4] == jaky_hrac and kameny[6] == jaky_hrac:
    return False
  else:
    return True


def vypln_hraci_kostku(tahy,kostka_data) -> list:
  """ funkce zapisuje do hraci kostky tahy hracu"""
  radek = [1,3,5]
  for cislo_radku in radek:
    znaky_radku = kostka_data[cislo_radku][1]
    nove_znaky = ''
    for i,znak in enumerate(znaky_radku):
      if cislo_radku == 1:
        pozice = 0 
      if cislo_radku == 3:
        pozice = 3
      if cislo_radku == 5:
        pozice = 6
      if i == 2:
        nove_znaky += tahy[pozice]
      elif i == 6:
        nove_znaky += tahy[pozice+1]
      elif i == 10:
        nove_znaky += tahy[pozice+2]
      else:
        nove_znaky += znak
    kostka_data[cislo_radku][1] = nove_znaky
  return kostka_data


def main() -> None:
  text = 'Player o | Please enter your move number: 5'
  delka = len(text)+1
  data = [['','+---+---+---+',''],
          ['','|   |   |   |',''],
          ['','+---+---+---+',''],
          ['','|   |   |   |',''],
          ['','+---+---+---+',''],
          ['','|   |   |   |',''],
          ['','+---+---+---+','']]
  delka_znaku = len(data[0][1])
  centr = uvod(delka)
  centrovani = centrovani_textu(delka,delka_znaku)
  tisk_hraci_kostky(data,centrovani)
  hra = True
  pole = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
  zacatek = True
  pocitadlo = 1
  hrac = 'o'
  kostka = {}
  while hra:
    zacatek = True
    print('=' * delka)
    volba = input(f'Player {hrac} | Please enter your move number: ')
    print('=' * delka)
    if je_cislo(volba):
      volba = int(volba)
      if osetreni_cisla(volba):
        if pole[volba-1] == ' ':
          pole[volba-1] = hrac
          kostka = vypln_hraci_kostku(pole,data)
          tisk_hraci_kostky(kostka,centrovani)
        else:
          print('{:^{delka_textu}}'.format('Array is full',**centr))
          print('{:^{delka_textu}}'.format(f'='*len('Array is full'),**centr))
          tisk_hraci_kostky(kostka,centrovani)
          zacatek = False
    if zacatek:
      hra = konec_hry(pole,hrac)
      pocitadlo += 1
      if hra:
        if hrac == 'x':
          hrac = 'o'
        else:
          hrac = 'x'
    if hra == False:
      print('=' * delka)
      print('{:^{delka_textu}}'.format(f'Congratulations, the player {hrac} WON!',**centr))
      print('=' * delka)
    if ' ' not in pole and hra:
      print('=' * delka)
      print('{:^{delka_textu}}'.format('DRAW GAME',**centr))
      print('=' * delka)
      hra = False


main()