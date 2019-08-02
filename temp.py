l = """Panharmonicon""".splitlines()



import urllib.request
import json
finals = []
for cname in l:
    # incomplete = True
    while True:
        try:
            link = "https://api.scryfall.com/cards/named?exact=" + '+'.join(cname.split(' '))
            response = urllib.request.urlopen(link)
            break
        except:
            cname = input("Error on {}, reinput card name: ".format(cname))
    html = response.read()
    data = json.loads(html.decode())
    print("{}\t{}".format(cname, data["prices"]["usd"]))
    finals.append("{}\t{}".format(cname, data["prices"]["usd"]))

with open("out.dat",'w') as fout:
    fout.write('\n'.join(finals))