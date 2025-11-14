#1
a=['admin','operator']
a.append('mike')
print(a)

#2
a=['root','security']
a.insert(0,'superuser')
print(a)

#3
a=['bob','charlie','alice']
a.remove('alice')
print(a)

#4
logs=['Access granted', 'Login failed','Connection lost']
a=logs.pop()
print('Последняя запись:',a)
print('Оставшиеся логи:',logs)

#5
a=['ok','error','ok','error','error']
a=a.count('error')
print('Количество ошибок входа:',a)

#6
a=['Access ok','Breach detected','System reboot','Breach detected']
a=a.index('Breach detected')
print('Первое обнаружение вторжения на позиции:',a)

#7
a=[3,1,2,3,1,2]
a.sort()
print(a)

#8
a=['2025-10-01', '2025-10-02', '2025-10-03']
a.reverse()
print(a)

#9
a=["alert","spam","login","error","spam","alert"]
a.remove('spam')
a.append('END_LOG')
a.reverse()
b=a.count('alert')
print('Журнал после очистки:',a)
print('Количество alert :',b)

#10
whitelist = ['192.168.0.1', '192.168.0.2', '192.168.0.3', '192.168.0.4', '192.168.0.5']
a=input("Введите IP для удаления: ")
b=input("Введите новый IP: ")
whitelist.remove(a)
whitelist.insert(2,b)
whitelist.sort()
c=whitelist.index(b)
print("Обновлённый белый список:", whitelist)
print("Индекс нового IP:",c)

#11
a=['ok','fail','fail','ok','fail']
b=a.count('fail')
while 'fail' in a:
    a.remove('fail')
a.append('audit_completed')
a.reverse()
c=a.index('ok')
print('Количество неудачных входов:',b)
print('Итоговый список:',a)
print('Первый индекс ok:',c)



