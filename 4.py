import random
f = open('scientist.txt', encoding='UTF8').read()  #Считываем, а после преобразовываем файл для использования
f = f.split('\n')
m = []
for i in f:
    m.append(i.split('#'))
def login(x): #Создаем логин
    x = x.split(' ')
    return x[0] + '_' + x[1][0] + x[2][0]
def password(): #Создаем пароль
    Alphabet1 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    Alphabet2 = 'qwertyuiopasdfghjklzxcvbnm'
    Alphabet3 = '0123456789'
    a1 = Alphabet1[random.randint(0, len(Alphabet1) - 1)]
    a2 = Alphabet1[random.randint(0, len(Alphabet1) - 1)]
    a3 = Alphabet1[random.randint(0, len(Alphabet1) - 1)]
    a4 = Alphabet1[random.randint(0, len(Alphabet1) - 1)]
    b1 = Alphabet2[random.randint(0, len(Alphabet2) - 1)]
    b2 = Alphabet2[random.randint(0, len(Alphabet2) - 1)]
    b3 = Alphabet2[random.randint(0, len(Alphabet2) - 1)]
    b4 = Alphabet2[random.randint(0, len(Alphabet2) - 1)]
    c1 = Alphabet3[random.randint(0, len(Alphabet3) - 1)]
    c2 = Alphabet3[random.randint(0, len(Alphabet3) - 1)]
    return a1 + a2 + a3 + a4 + b1 + b2 + b3 + b4 + c1 + c2
for i in m: 
    i.append(login(i[0]))
    i.append(password())
f = open('scientist_password.csv', 'w', encoding='UTF8')
for i in m: #Записываем в файл
    f.write('#'.join(i) + '\n')

