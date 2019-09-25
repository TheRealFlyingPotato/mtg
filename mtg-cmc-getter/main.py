import funcs
import requests
import sys

################
action = funcs.getUSD # funcs.getCMC, funcs.getUSD
################

# input('|'.join(sys.argv))

with open(sys.argv[1], 'r') as fin:
  lines = fin.readlines()

with open('out.dat', 'w') as fout:
  for line in lines:
    card = line.strip()
    card = funcs.removeCount(card)
    cont = True
    while cont:
      resp = requests.get('https://api.scryfall.com/cards/named?exact="' + card + '"')
      if resp.status_code == 200:
        cardData = resp.json()
        card = cardData['name']
        success, val = action(cardData)
        if success:
          print(val)
          fout.write("{}\n".format(val))
          cont = False
        else:
          card = val
      else:
        success, val = funcs.wrongName(card)
        if success:
          print(val)
          fout.write(val)
          cont = False
        else:
          card = val

        # print(card, resp.status_code)
        # cardData = resp.json()
      

