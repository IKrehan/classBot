from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time
import getpass
from os import system


classes = [
    {
        '13:40': 'Compreensão Textual II',
        '14:30': 'Física I',
        '15:20': 'Gramática',
        '16:00': 'Intervalo',
        '16:40': 'Física II',
        '17:30': 'Compreensão Textual I',
        '18:20': 'Física III',
        '19:00': 'Fim'
    },

    {
        '13:40': 'Química I',
        '14:30': 'Matemática I',
        '15:20': 'Matemática II',
        '16:00': 'Intervalo',
        '16:40': 'Geografia II',
        '17:30': 'Física IV',
        '18:20': 'Química IV',
        '19:00': 'Fim'
    },

    {
        '13:40': 'Filosofia/Sociologia',
        '14:30': 'Química II',
        '15:20': 'História I',
        '16:00': 'Intervalo',
        '16:40': 'História I',
        '17:30': 'Biologia IV',
        '18:20': 'Química III',
        '19:00': 'Fim'
    },

    {
        '13:40': 'Geografia I',
        '14:30': 'Matemática III',
        '15:20': 'Redação',
        '16:00': 'Intervalo',
        '16:40': 'Matemática IV',
        '17:30': 'Biologia III',
        '18:20': 'Matemática V',
        '19:00': 'Fim'
    },

    {
        '13:40': 'Língua Estrangeira',
        '14:30': 'Literatura',
        '15:20': 'História II',
        '16:00': 'Intervalo',
        '16:40': 'Biologia I',
        '17:30': 'Biologia II',
        '18:20': 'Matemática Básica',
        '19:00': 'Fim'
    },
]

links = {
    'Química IV': 'https://meet.google.com/lookup/bsodzydalx?authuser=1&hs=179',
    'Química III': 'https://meet.google.com/lookup/argmwvm4bw?authuser=1&hs=179',
    'Química II': 'https://meet.google.com/lookup/cllqonh4qe?authuser=1&hs=179',
    'Química I': 'https://meet.google.com/lookup/cipttucbzn?authuser=1&hs=179',
    'Física IV': 'https://meet.google.com/lookup/huaxeibkzr?authuser=1&hs=179',
    'Física III': 'https://meet.google.com/lookup/fof634akcj?authuser=1&hs=179',
    'Física II': 'https://meet.google.com/lookup/fknwwdfu5a?authuser=1&hs=179',
    'Física I': 'https://meet.google.com/lookup/ejfvtki3nw?authuser=1&hs=179',
    'Biologia IV': 'https://meet.google.com/lookup/e2emxbpodr?authuser=1&hs=179',
    'Biologia III': 'https://meet.google.com/lookup/cajn27nkru?authuser=1&hs=179',
    'Biologia II': 'https://meet.google.com/lookup/ezn5q3hatz?authuser=1&hs=179',
    'Biologia I': 'https://meet.google.com/lookup/feeooc7ltq?authuser=1&hs=179',

    'Matemática Básica': 'https://meet.google.com/lookup/bb4h6w4rwf?authuser=1&hs=179',
    'Matemática V': 'https://meet.google.com/lookup/hehjht37ga?authuser=1&hs=179',
    'Matemática IV': 'https://meet.google.com/lookup/bs2nodzdvi?authuser=1&hs=179',
    'Matemática III': 'https://meet.google.com/lookup/dc3u2wphcd?authuser=1&hs=179',
    'Matemática II': 'https://classroom.google.com/u/1/c/ODMyNjQxNDU5Mjha',
    'Matemática I': 'https://meet.google.com/lookup/alfsk73vxa?authuser=1&hs=179',

    'Literatura': 'https://meet.google.com/lookup/er6mlv5yw2?authuser=1&hs=179',
    'Gramática': 'https://meet.google.com/lookup/hy5b263a3z?authuser=1&hs=179',
    'Compreensão Textual II': 'https://meet.google.com/lookup/fv6i64zzaj?authuser=1&hs=179',
    'Compreensão Textual I': 'https://meet.google.com/lookup/htvagz257b?authuser=1&hs=179',
    'Espanhol': 'https://meet.google.com/lookup/cjxxegn4ei?authuser=1&hs=179',
    'Redação': 'https://meet.google.com/lookup/eestadq57g?authuser=1&hs=179',

    'História II': 'https://meet.google.com/lookup/d2f26gbbbr?authuser=1&hs=179',
    'História I': 'https://meet.google.com/lookup/a7xdh5tcdx?authuser=1&hs=179',
    'Geografia II': 'https://meet.google.com/lookup/fizdlwool5?authuser=1&hs=179',
    'Geografia I': 'https://meet.google.com/lookup/fizdlwool5?authuser=1&hs=179',
    'Filosofia/Sociologia': 'https://meet.google.com/lookup/eb7cifcn5n?authuser=1&hs=179',
}

header = '''
===================================================================================================
===================================================================================================

   @@@@@@@@@@   @@@      @@@@@@@        .@@@@@@@@  @@@@@@@@@ @@@@@@@@@    .@@@@@@@@@@.  @@@@@@@@@@ 
 @@@@     @@@@  @@@      @@@'@@@@       @@@       @@@@              @@@  &@@@      @@@@    @@@@    
 @@@            @@@      @@@  @@@@       @@@@@@    @@@@@@    @@@@@@@@@   @@@        @@@@   @@@@    
 @@@        @@@ @@@      @@@   @@@@          @@@@       @@@@        @@@  @@@&       @@@    @@@@    
  @@@@    @@@@  @@@@@@@@ @@@@@@@@@@@         @@@@       @@@@ @@@@@@@@@    @@@@@@@@@@@@     @@@@    
     @@@@@@     @@@@@@@@ @@@      @@@,  @@@@@@@%  @@@@@@@@   @@@@@@@@        @@@@@@,       @@@@  

===================================================================================================
===================================================================================================
'''


def enterClass(currentClass, driver):
    # Entra na sala
    driver.get('https://meet.google.com/lookup/feeooc7ltq?authuser=1&hs=179')

    time.sleep(5)
    if driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div'):
        driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div').click()

    enter_button = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
    enter_button.click()


def quitClass(driver):
    driver.get('https://accounts.google.com/')


print(header)
print('\n')

email = str(input('Email: '))        # 260300@aluno.colegioprovecto.com.br
password = str(input('Senha: '))        # 27122002
print('\n')

system('cls')

print(header)
print('\n')

driver = webdriver.Firefox()

# Loga no google
driver.get('https://accounts.google.com/')

driver.find_element_by_name('identifier').send_keys(email, Keys.RETURN)
time.sleep(2)

driver.find_element_by_name('password').send_keys(password, Keys.RETURN)
time.sleep(5)

animation = "|/-\\"
idx = 0
while True:

    weekday = datetime.now().weekday()
    now = f'{datetime.now().hour}:{datetime.now().minute}'
    dayClasses = classes[weekday]

    if now in dayClasses:
        if now == '16:00':
            quitClass(driver)

        if now == '19:00':
            break


        try:
            enterClass(dayClasses[now], driver)
        
        except:
            time.sleep(5)
            enterClass(dayClasses[now], driver)

    print(animation[idx % len(animation)],'RODANDO...' , end="\r")
    idx += 1
    time.sleep(0.1)