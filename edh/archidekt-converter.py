import sys

fname = sys.argv[1]

with open(fname,'r') as fin:
  data = fin.readlines()
with open('output', 'w') as fout:
  for line in data:
    print([line])
    if "###" in line:
      category = line[3:].strip()
      continue
    if line[0] in ['\n', '#']:
      continue
    fout.write('{} `{}`\n'.format(line.strip(), category))
  