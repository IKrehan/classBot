from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.keys import Keys
import time
import getpass
from os import system
import ast


classes_file = open("aulas.txt", "r")
classes = ast.literal_eval(classes_file.read())
classes_file.close()

links_file = open("links.txt", "r")
links = ast.literal_eval(links_file.read())
links_file.close()

days = {
    0: "Segunda-Feira",
    1: "Terça-Feira",
    2: "Quarta-Feira",
    3: "Quinta-Feira",
    4: "Sexta-Feira",
    5: "Sábado",
    6: "Domingo",
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

email = str(input('Email: '))
password = str(input('Senha: '))
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

    if weekday < 4:
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

    print(f"{days[weekday]} {now}  ", animation[idx % len(animation)],'RODANDO...' , end="\r")
    idx += 1
    time.sleep(0.1)