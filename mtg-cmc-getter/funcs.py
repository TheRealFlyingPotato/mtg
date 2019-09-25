### Return statuses:
###    True : success, returns string to write to file
###    False : error, returns new name for scryfall api lookup
def getCMC(json):
  if 'cmc' in json.keys():
    return 1, '{}\t{}'.format(json['name'], int(json['cmc']))
  return wrongName(json['name'])

def getUSD(json):
  if 'prices' in json.keys():
    if 'usd' in json['prices'].keys():
      if 'usd_foil' in json['prices'].keys():
        return 1, '{}\t{}\t{}'.format(json['name'], json['prices']['usd'], json['prices']['usd_foil'])


def removeCount(c):
  l = c.split(' ')
  try:
    int(l[0])
    return ' '.join(l[1:])
  except:
    return c


def wrongName(name):
  inp = input("Error on {}. Input card name or manual data:\n".format(name))
  try:
    inp = int(inp)
    return 1, ('{}\t{}'.format(name, inp))
  except:
    return 0, inp