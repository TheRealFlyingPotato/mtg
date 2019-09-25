import os

def main():
  files = os.listdir()
  cardLists = []
  for f in files:
    if f == os.path.basename(__file__) or f == "shared.dat" or f == "only0.dat" or f == "only1.dat":
      continue
    with open(f, 'r') as fin:
      cardLists.append(fin.readlines())
  with open("shared.dat", 'w') as sharedout:
    with open("only0.dat", 'w') as only0out:
      for card in cardLists[0]:
        if card in cardLists[1]:
          sharedout.write(card)
        else:
          only0out.write(card)
  with open("only1.dat",'w') as only1out:
    for card in cardLists[1]:
      if card not in cardLists[0]:
        only1out.write(card)




if __name__ == "__main__":
    main()    