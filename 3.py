f = open('scientist.txt', encoding='UTF8').read() #Считываем, а после преобразовываем файл для использования
f = f.split('\n')
m = []
for i in f:
    m.append(i.split('#'))
s = ''
def shortname(x): #Функция для укорачивания ФИО
    x = x.split(' ')
    return x[0] + ' ' + x[1][0] + '.' + x[2][0] + '.'
while True: #Основной код
    if s == 'эксперимент':
        break
    s = input() #Принимаем от пользователя запрос
    mark = False
    for i in m:
        if i[2] == s:
            name = shortname(i[0])
            id = i[1]
            date = s
            print(f'“Ученый {name} создал препарат: {id} - {date}”') #Выводим результат
            mark = True
    if mark == False:
        print('В этот день ученые отдыхали')  #Выводим результат
