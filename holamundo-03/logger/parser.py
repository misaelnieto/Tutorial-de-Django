import re

regex = re.compile('^([\\d.]+) (\\S+) (\\S+) \\[([\\w:/]+\\s[+\\-]\\d{4})\\] \"(.+?)\" (\\d{3}) (\\d+) \"([^\"]+)\" \"([^\"]+)\"')

def parsear(linea):
    m = regex.match(linea)
    if m:
        return m.groups()
    else:
        return ()

