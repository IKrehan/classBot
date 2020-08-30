from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep, strftime, localtime

from os import system
import ast

classes_file = open("aulas.txt", "r")
classes = ast.literal_eval(classes_file.read())
classes_file.close()

links_file = open("links.txt", "r")
links = ast.literal_eval(links_file.read())
links_file.close()

days = {
    0: "Domingo",
    1: "Segunda-Feira",
    2: "Terça-Feira",
    3: "Quarta-Feira",
    4: "Quinta-Feira",
    5: "Sexta-Feira",
    6: "Sábado",
}


header = ('''
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
''')

def loginUser(email, password, driver):
    try:
        # Loga no google
        driver.get('https://accounts.google.com/')

        driver.find_element_by_name('identifier').send_keys(email, Keys.RETURN)
        sleep(2)

        driver.find_element_by_name('password').send_keys(password, Keys.RETURN)
        sleep(5)
    
    except:
        loginUser(email, password, driver)


def enterClass(currentClass, driver):
    try:
        # Entra na sala
        driver.get(links[currentClass])

        sleep(5)

        enter_button = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]')
        enter_button.click()
        sleep(60)
    
    except:
        enterClass(currentClass, driver)



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

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--use-fake-ui-for-media-stream")

driver = webdriver.Chrome(options=options)

loginUser(email, password, driver)

animation = "|/-\\"
idx = 0
while True:
    date = localtime()
    weekday = int(strftime("%w", date))
    now = strftime("%H:%M", date)

    print(f"{days[weekday]} {now}  ", animation[idx % len(animation)],'RODANDO...' , end="\r")
    idx += 1
    sleep(0.1)


    if weekday > 0 and weekday <= 5:
        dayClasses = classes[weekday]

        if now in dayClasses:
            enterClass(dayClasses[now], driver)
