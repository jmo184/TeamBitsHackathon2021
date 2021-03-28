# PYTHON PROGRAM GUESSING GAME
# CHOOSE AN NBA PLAYER THAT MAY SCORE
# THE HIGHEST AMOUNT OF POINTS TODAY


from selenium import webdriver
from datetime import datetime
from os import path
import os.path
from datetime import datetime

import time
from tkinter import *

now = datetime.now()
time_string = now.strftime("%H %M %S")
time_cut = time_string.split()

totalTime = time_cut[0] + time_cut[1]

userGuess = input("Who will score the most points in the NBA today? ")


x = totalTime

today = datetime.now()

todaydate = datetime.today().strftime('%m-%d')

name = "guessOn"+todaydate+".txt"

if os.path.isfile(name):
    print("You entered an answer for today! Using " + name)

else:
    print("Creating file...")
    f = open(name, "w")
    f.write(userGuess)

with open(name, 'r') as file:
    userGuess = file.read()

print(userGuess)

if int(time_cut[0]) > 12:
    timeHour = int(time_cut[0]) - 12

options = webdriver.ChromeOptions()

# USE FOR OPENING WINDOW #
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches", ["enable-automation"])

# USE FOR HIDDEN WINDOW #
options.add_argument('headless')

driver_path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get('https://www.google.com/search?q=top+scorer+in+nba+today&source=hp&ei=U0hdYIb2G47-tAXnnr3QDA&iflsig=AINFCbYAAAAAYF1WYwDsgIPg1MPPULoPprYkOd78wvhP&oq=top+scorer+in+nba+t&gs_lcp=Cgdnd3Mtd2l6EAMYAjICCAAyAggAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOggIABCxAxCDAToLCC4QsQMQxwEQowI6BQgAELEDOggILhCxAxCTAjoFCC4QsQM6DgguELEDEIMBEMcBEKMCOggILhDHARCjAjoOCC4QsQMQxwEQowIQkwI6CAguEMcBEK8BOgoIABCxAxCDARAKOhAILhCxAxDHARCvARAKEJMCOggIABCxAxDJAzoFCAAQkgM6BAgAEAo6BQgAEIYDUJOsJlj72CZgwegmaANwAHgAgAF4iAGSC5IBBDIwLjGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=gws-wiz')

nameAndPoints = driver.find_element_by_xpath('/html/body/div[8]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[1]/div/div/div[1]').text
dateOfScore = driver.find_element_by_xpath('/html/body/div[8]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/span[3]/span').text

# driver.close()

nameSplit = nameAndPoints.split()

topScorer = nameSplit[0] + " " + nameSplit[1]


if nameSplit[3] == '·':
    totalPoints = nameSplit[4]
else:
    totalPoints = nameSplit[3]


print(topScorer + " was the Top Scorer in the NBA today with " + totalPoints + " points on " + dateOfScore)

if userGuess.casefold() == topScorer.casefold():
    print("YOU GUESSED RIGHT! CONGRATULATIONS")
else:
    print("YOU GUESSED WRONG! TRY AGAIN")

print("time played at " + str(timeHour) + ":" + time_cut[1])
