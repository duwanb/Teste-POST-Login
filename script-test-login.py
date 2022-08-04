import requests
from re import search



word = 'Your username or password is incorrect'

#listausers = [('teste', 'teste'), ('teste2.teste2', 'teste2.teste2')]
my_file = open("lista_users.txt", "r")
content = my_file.read()
content_list = content.split("\n")

file = open('lista-users-senhafraca.txt', 'w')


for i in content_list:
    url = 'URL LOGIN'
    myobj = {'user': i , 'pass' : i}
    #myobj = {'user': i[0] , 'pass' : i[1]}

    x = requests.post(url, data=myobj, json = myobj)
    #print(i[0])
    if not search(word, x.text):
        file.write(str(i)+" -------- SENHA FRACA\n")
        
my_file.close()
file.close()