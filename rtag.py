#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import requests, re, random, os, subprocess, paramiko, base64, sys


chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
otv =[]
ot = []
data =[]


print('')
print('')
print('')
print (' $$$$$$\  $$$$$$\ $$$$$$$\         $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ ')
print ('$$  __$$\ \_$$  _|$$  __$$\       $$  __$$\ $$  __$$\ $$$\  $$ |$$  _____|')
print ('$$ /  \__|  $$ |  $$ |  $$ |      $$ /  \__|$$ /  $$ |$$$$\ $$ |$$ |      ')
print ('\$$$$$$\    $$ |  $$$$$$$  |      $$ |      $$ |  $$ |$$ $$\$$ |$$$$$\    ')
print (' \____$$\   $$ |  $$  ____/       $$ |      $$ |  $$ |$$ \$$$$ |$$  __|   ')
print ('$$\   $$ |  $$ |  $$ |            $$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |      ')
print ('\$$$$$$  |$$$$$$\ $$ |            \$$$$$$  | $$$$$$  |$$ | \$$ |$$ |      ')
print (' \______/ \______|\__|             \______/  \______/ \__|  \__|\__|      ')
print('')
print('')
print('')
print('')


secret_open = open('pass_.txt') #открываем файл пароль
secret = secret_open.read() #читаем файл пароль

secret_split = secret.split(':') #режим на строки

user_secret = secret_split[0] #лого
pass_secret = secret_split[1] #пасс


number = input('Enter number: ') #номер телефона
dogovor = input('Enter dogovor: ') #договор, пока так
ext_ip = raw_input ('Enter ext IP: ') #внешний ip

ex = ext_ip.split() #делим на строки внешние ip
st_ex = len(ex) #смотрим сколько строк получилось

#заголовок для запроса
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
#передаем параметры
params = (
    ('module', 'sip'),
    ('show', 'action'),
    ('sql', 'search'),
)

respo = 'http://' + secret + '@rtag.novotelecom.ru/1.php' #клеим запрос с паролем
resp = ''.join(respo) #убираем пробелы из запроса

#массив для номера
data = {
    'name': 'num'
	}
data['name'] = number #добавляем номер который ввели

response = requests.post( resp, headers=headers, params=params, data=data) #запрос на получение данные из биллинга

response = response.content #читаем что в ответе
respo = response.split() #делим построчно

for i in range(len(respo)): #читаем построчный ответ
    y = respo[i].find('left')  #ищем left
    if y != -1 :
	otv.append(respo[i]) #добавляем найденной в новый массив
 
for i in range(len(otv)):  #удаляем лишнее
    y = otv[i].replace('align="left">','').replace('</td>','').replace('<tr><td','')
    ot.append(y)

ot = [x.strip('') for x in ot] #что-то  клием

#формируем строки из биллинга
ipadd_bill = ot[1]  #ip default
context_bill = ot[2] #context
limit_bill = ot[3] #call limit
setvar = ot[4] #setvar
setvar_bill = setvar.split(';') #setvar режим по строчно, если их там больше одного

#генерация пароля. 1 штука, 8 символов
for n in range(1):
    password =''
    for i in range(10):
        password += random.choice(chars)

#хуячество, можно сделать изящнее, но пока не понял как
pref = str(383) #префикс
num = str(number) #переводим номер в строку
nomer = pref + num #клеим
num = '[',pref + num,']' #генерцаия с квадратными скобками
nomer_bill = ''.join(num) #без кв скобок
dog1 = str(dogovor) #договор в строку
dog_pre = ';',dog1 #добавления тчк
dog = ''.join(dog_pre) #удаления пробела
ipadd_bi = ipadd_bill,'/255.255.255.255' #IP и маска
ipa_bi = ''.join(ipadd_bi)
ext_ip2 = ext_ip,'/255.255.255.255'
ext_i = ''.join(ext_ip2)
username_1 = ['username = ',nomer]
username_sip = ''.join(username_1)
secret_1 = ['secret = ',password]
secret_sip = ''.join(secret_1)
accountcode_1 = ['accountcode = ',nomer]
accountcode_sip = ''.join(accountcode_1)
callerid_1 = ['callerid = ',nomer]
callerid_sip = ''.join(callerid_1)
defa_ip = ['defaultip = ',ipadd_bill]
dafault_ip_sip = ''.join(defa_ip)
ipa_1 = ['permit = ',ipa_bi]
ipadd_sip = ''.join(ipa_1)
ext_1 = ['permit = ',ext_i]
ext_sip = ''.join(ext_1)
limit_1 = ['call-limit = ',limit_bill]
limit_sip = ''.join(limit_1)
st = len(setvar_bill)
if st == 2:
    setvar_si1 ='setvar = ',setvar_bill[0]
    setvar_sip1 = ''.join(setvar_si1)
    setvar_si2 ='setvar = ',setvar_bill[1]
    setvar_sip2 = ''.join(setvar_si2)
if st == 3:
    setvar_si1 ='setvar = ',setvar_bill[0]
    setvar_sip1 = ''.join(setvar_si1)
    setvar_si2 ='setvar = ',setvar_bill[1]
    setvar_sip2 = ''.join(setvar_si2)
    setvar_si3 ='setvar = ',setvar_bill[2]
    setvar_sip3 = ''.join(setvar_si3)
if st_ex == 1:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
if st_ex == 2:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
if st_ex == 3:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
    ex_i_3 = 'permit = ',ex[2],'/255.255.255.255'
    ex_ext_3 = ''.join(ex_i_3)
if st_ex == 4:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
    ex_i_3 = 'permit = ',ex[2],'/255.255.255.255'
    ex_ext_3 = ''.join(ex_i_3)
    ex_i_4 = 'permit = ',ex[3],'/255.255.255.255'
    ex_ext_4 = ''.join(ex_i_4)
if st_ex == 5:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
    ex_i_3 = 'permit = ',ex[2],'/255.255.255.255'
    ex_ext_3 = ''.join(ex_i_3)
    ex_i_4 = 'permit = ',ex[3],'/255.255.255.255'
    ex_ext_4 = ''.join(ex_i_4)
    ex_i_5 = 'permit = ',ex[4],'/255.255.255.255'
    ex_ext_5 = ''.join(ex_i_5)
if st_ex == 6:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
    ex_i_3 = 'permit = ',ex[2],'/255.255.255.255'
    ex_ext_3 = ''.join(ex_i_3)
    ex_i_4 = 'permit = ',ex[3],'/255.255.255.255'
    ex_ext_4 = ''.join(ex_i_4)
    ex_i_5 = 'permit = ',ex[4],'/255.255.255.255'
    ex_ext_5 = ''.join(ex_i_5)
    ex_i_6 = 'permit = ',ex[5],'/255.255.255.255'
    ex_ext_6 = ''.join(ex_i_6)
if st_ex == 7:
    ex_i_1 = 'permit = ',ex[0],'/255.255.255.255'
    ex_ext_1 = ''.join(ex_i_1)
    ex_i_2 = 'permit = ',ex[1],'/255.255.255.255'
    ex_ext_2 = ''.join(ex_i_2)
    ex_i_3 = 'permit = ',ex[2],'/255.255.255.255'
    ex_ext_3 = ''.join(ex_i_3)
    ex_i_4 = 'permit = ',ex[3],'/255.255.255.255'
    ex_ext_4 = ''.join(ex_i_4)
    ex_i_5 = 'permit = ',ex[4],'/255.255.255.255'
    ex_ext_5 = ''.join(ex_i_5)
    ex_i_6 = 'permit = ',ex[5],'/255.255.255.255'
    ex_ext_6 = ''.join(ex_i_6)
    ex_i_7 = 'permit = ',ex[6],'/255.255.255.255'
    ex_ext_7 = ''.join(ex_i_7)

if context_bill != 0: #если контекст из биллиенга не равен нулю, тогда генерируем
	cont_1 =['context = ',context_bill]
	context_sip = ''.join(cont_1)




#показываем сформировнный на экране
#sip_generator = open("sip_generator.txt", "w") #открывем file sip_generator.txt
#sip_generator.write(str(nomer_bill)) #записываем в sip_generator.txt
#sip_generator.write(str(dog)) #записываем в sip_generator.txt
#sip_generator.write(str(username_sip)) #записываем в sip_generator.txt
#sip_generator.close() #закрываем файл




print ('')
print ('')
print ('')
print ('')
print ('~~~~~SIP conf~~~~~')
print ('')
print ('')
print nomer_bill
print dog
print ('type = friend')
print username_sip
print secret_sip
print accountcode_sip
print callerid_sip
print ('host = dynamic')
print dafault_ip_sip
print ('deny = 0.0.0.0/0.0.0.0')
print 'permit =',ipa_bi
if st_ex == 1:
    print ex_ext_1
if st_ex == 2:
    print ex_ext_1
    print ex_ext_2
if st_ex == 3:
    print ex_ext_1
    print ex_ext_2
    print ex_ext_3
if st_ex == 4:
    print ex_ext_1
    print ex_ext_2
    print ex_ext_3
    print ex_ext_4
if st_ex == 5:
    print ex_ext_1
    print ex_ext_2
    print ex_ext_3
    print ex_ext_4
    print ex_ext_5
if st_ex == 6:
    print ex_ext_1
    print ex_ext_2
    print ex_ext_3
    print ex_ext_4
    print ex_ext_5
    print ex_ext_6
if st_ex == 7:
    print ex_ext_1
    print ex_ext_2
    print ex_ext_3
    print ex_ext_4
    print ex_ext_5
    print ex_ext_6
    print ex_ext_7
if context_sip != 0:
	print context_sip
if st == 2:
        print setvar_sip1
        print setvar_sip2
if st == 3:
        print setvar_sip1
        print setvar_sip2
        print setvar_sip3
print ('disallow = all')
print ('allow = alaw')
print ('allow = ulaw')
print limit_sip
print ('canreinvite = no')
print ('nat = yes')
print ('~~~~~~~~~~~~~~~~')
print ('')
print ('')
print ('')
print ('')
print ('~~~~~Отсылаем клиенту~~~~~')
print ('Адрес для поднятия регистрации sipserver.novotelecom.ru')
print 'username =',nomer
print 'secret =',password
print ('')
print ('')

#route  = input('Прокинуть ip?( y/n): ') #спрашиваем о пробросе 
#print ('')
#print ('')
#if route == y:
#    print ('Запуск проброса')
#    print ('')
#    route_go = os.system("bash add.sh " + ex_i_r) #отдаем данные скрипту для проброса
#else:
#    print ('Ок')


#сбор в файл sip.conf

if st == 0:
    st1 = st
if st == 1:
    sip_conf_genera = [nomer_bill, dog, 'type = friend', username_sip, secret_sip, accountcode_sip, callerid_sip, 'host = dynamic', dafault_ip_sip, 'deny = 0.0.0.0/0.0.0.0', context_sip, 'disallow = all', 'allow = alaw', 'allow = ulaw', limit_sip, 'canreinvite = no', 'nat = yes', ex_ext_1, setvar_sip1]
if st == 2:
    sip_conf_genera = [nomer_bill, dog, 'type = friend', username_sip, secret_sip, accountcode_sip, callerid_sip, 'host = dynamic', dafault_ip_sip, 'deny = 0.0.0.0/0.0.0.0', context_sip, 'disallow = all', 'allow = alaw', 'allow = ulaw', limit_sip, 'canreinvite = no', 'nat = yes', ex_ext_1, setvar_sip1, setvar_sip2]
if st == 3:
    sip_conf_genera = [nomer_bill, dog, 'type = friend', username_sip, secret_sip, accountcode_sip, callerid_sip, 'host = dynamic', dafault_ip_sip, 'deny = 0.0.0.0/0.0.0.0', context_sip, 'disallow = all', 'allow = alaw', 'allow = ulaw', limit_sip, 'canreinvite = no', 'nat = yes', ex_ext_1, setvar_sip1, setvar_sip2,setvar_sip3]



#проверка в sip.conf на asterisk

host_sip1 = 'sipserver1.core'
host_sip2 = 'sipserver2.core'
command_sip_from_host = 'grep', nomer, '/etc/asterisk/sip.conf -A17 -B1'
command_find = ' '.join(command_sip_from_host)
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host_sip2, username=user_secret, password=pass_secret, look_for_keys=False, allow_agent=False)
stdin, stdout, stderr = client.exec_command(command_find)
data_search_from_sipserver = stdout.read() + stderr.read()
client.close()

#list_sip_conf_genera=sip_conf_genera.split()
#list_data_search_from_sipserver=data_search_from_sipserver.split()

data_search_from_sipserver_split=data_search_from_sipserver.split('\n')#нарезали строчно

print ('Данные на sipserver')
print data_search_from_sipserver
print ('~~~~~~~~~~~~~~~~')
print ('')
print ('')
print ('')

diff_list=list(set(sip_conf_genera) - set(data_search_from_sipserver_split))
print ('Нужно добавить в sip.conf')

#for i in range(len(diff_list)): #читаем построчный ответ
#    y = diff_list[i].find(',')  #ищем запятая
#    if y != -1 :
#    diff_list_print( diff_list[i]) #добавляем найденной в новый массив

print(diff_list)
print ('')
print ('')




#si_open = open('pass_.txt') #открываем файл пароль
#secret = secret_open.read() #читаем файл пароль



#if len(data_search_from_sipserver) != 0:
#    print ('В sip.conf есть есть по этому номеру. Добавить новые данные?')
#    print (data_search_from_sipserver)
#if len(data_search_from_sipserver) == 0:
#    print ('Различий нет')

#вытаскиваем diff
#print('Различия епта')
#diff_sip = list(set(data_search_from_sipserver) - set(sip_conf_genera))
#diff = ''.join(diff_sip)
#print diff


route  = input('Прокинуть ip?( y/n): ')
print ('')
print ('')
#command = 'bash add.s', ex_i_r
#com = ' '.join(command)
if route == y:
    print ('Запуск проброса')
    print ('')
    route_go = os.system("bash add.sh " + ex_i_r)
else:
    print ('Ок')

