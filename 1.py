f = open('scientist.txt', encoding='UTF8').read()
f = f.split('\n')
m = []
for i in f:
    m.append(i.split('#'))
