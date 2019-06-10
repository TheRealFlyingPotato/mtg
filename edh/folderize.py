import os


def removeExtensions(n):
    return n.split(',')[0]

dir = os.listdir()
for name in os.listdir():
    if name == 'folderize.py':
        continue
    newName = removeExtensions(name)
    os.system('mv {} {}.tmp'.format(name, newName))
    os.system('mkdir {}'.format(newName))
    os.system('mv {}.tmp {}/{}.txt'.format(newName, newName, newName))