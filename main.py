# [Aula 01] -> Python Power Up: Automação de Tarefas

import pyautogui as pg 
from time import sleep
import pandas as pd


# *[Passo 01]: Entrar no sistema
#     lib => pyautogui
#     1. Abrir Navegador
#         1. apertar tecla [Windows] -> pyautogui.press("win")

#         2. Digitar 'Chrome'
       
def webDrive(link): #função para acessar o navegador
    pg.PAUSE = 0.5
    pg.press('win')
    pg.write("Chrome")
    pg.press('enter')
    sleep(1)
    access(link)
    
#     2. Entrar no link
#         1. Digitar link
#         2. Apertar tecla [Enter]
def access(link):
    pg.write(link)
    pg.press('enter')
    sleep(3)
  
   
# *[Passo 02]: Fazer login
#     1. Digitar email
#         1. Clicar no box email
#         2. Digitar o email
#         3. Apertar tecla [Tab]
    
#     2. Digital Senha
#         1. Digitar a Senha
#         2. Apertar tecla [tab]
#     3. Clicar em Login
#         1. Apertar tecla [Enter]
def login(email,pwd):
    pg.click(x=797, y=406) #encontra o campo de preenchimento do email  
    pg.write(email) #digita o email
    sleep(2)

    pg.press('tab') #passa para o próximo campo apenas usando a tecla [Tab]
    pg.write(pwd) #digita a senha
    sleep(2)

    pg.press('tab') #passa para o próximo campo apenas usando a tecla [Tab]
    pg.press('enter')


# *[Passo 03]: Importar a base de dados
#     lib = pandas
#     base de dados => produtos.csv

#     1. Ler a base de dados
#         tabela = pandas.read_csv("produtos.csv")
def getDatabase(db):
    table = pd.read_csv(db)
    print(table)
    return table


        


# *[Passo 04]: Cadastrar um produto
def registerData(db):
    table = getDatabase(db)
    for linha in table.index:
        pg.click(x=728, y=295)
        codigo = table.loc[linha,"codigo"]
        pg.write(str(codigo))
        pg.press('tab')
        
        pg.write(str(table.loc[linha,'marca']))
        pg.press('tab')
        
        pg.write(str(table.loc[linha,'tipo']))
        pg.press('tab')
        
        pg.write(str(table.loc[linha,'categoria']))
        pg.press('tab')
        
        pg.write(str(table.loc[linha,'preco_unitario']))
        pg.press('tab')
        
        pg.write(str(table.loc[linha,'custo']))
        pg.press('tab')
        obs = table.loc[linha,'obs']
        if not pd.isna(obs):#check se obs não é NaN
            pg.write(str(table.loc[linha,'obs']))
        pg.press('tab')
        
        pg.press('enter')
        pg.scroll(5000)
        
        

# *[Passo 05]: Repetir o processo de cadastro para todos os produtos




sys = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"  #sistema apenas para desenvolvimento da automação
email = 'banana@gmail.com' #email ficticio
pwd = 'senhaaleatoria' #senha ficticia
db = './gabarito/produtos.csv' #base de dados ficticia para desenvolvimento da automação

webDrive(sys)
login(email,pwd)
registerData(db)

    