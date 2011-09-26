import re

#regex = re.compile(r'\[(.*?)\]')
regex = re.compile(r'^\[(.*?)\]\s\[(.*?)\]\s(.*)')

def parsear(linea):
    m = regex.match(linea)
    if m:
        return m.groups()
    else:
        return ()

