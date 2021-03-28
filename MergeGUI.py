# PYTHON PROGRAM GUESSING GAME
# CHOOSE AN NBA PLAYER THAT MAY SCORE-
# -THE HIGHEST AMOUNT OF POINTS TODAY

from selenium import webdriver
from datetime import datetime
import tkinter as tk
from PIL import Image, ImageTk


def submit_guess(guess):
    if guess == '':  # If user enters a blank space, ask them to submit an NBA player's name
        label['text'] = "Please enter an NBA Player's first and last name"
    else:
        if get_time():  # Check to see if NBA games are still in progress
            label[
                'text'] = "You guessed " + guess + " to be the Top Scorer in the NBA today\nNBA games are in progress...\nCheck back later"
        else:
            find_top_scorer(guess)


def get_time():
    # Grab current time
    now = datetime.now()
    time_string = now.strftime("%H %M %S")
    time_cut = time_string.split()

    # Combine time(military) as a string
    total_time = time_cut[0] + time_cut[1]

    # Message user that NBA games have not finished playing yet
    # Compares current time to 11:00pm(When NBA games are guaranteed to be finished)
    if int(total_time) < 2100:
        return True

    # Change military time to normal civilian time
    if int(time_cut[0]) > 12:
        time_hour = int(time_cut[0]) - 12
        day_time = "PM"
    elif int(time_cut[0]) < 1:
        time_hour = int(time_cut[0]) + 12
        day_time = "AM"
    else:
        time_hour = int(time_cut[0])
        day_time = "AM"

    result_statement = "Time played at " + str(time_hour) + ":" + time_cut[1] + day_time
    print(result_statement)


def find_top_scorer(user_guess):

    # Open chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    # EXECUTE A CHROME GOOGLE SEARCH TO FIND THE NBA TOP SCORER
    url = 'https://www.google.com/search?q=top+scorer+in+nba+today&source=hp&ei=U0hdYIb2G47-tAXnnr3QDA&iflsig=AINFCbYAAAAAYF1WYwDsgIPg1MPPULoPprYkOd78wvhP&oq=top+scorer+in+nba+t&gs_lcp=Cgdnd3Mtd2l6EAMYAjICCAAyAggAMgIIADIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOggIABCxAxCDAToLCC4QsQMQxwEQowI6BQgAELEDOggILhCxAxCTAjoFCC4QsQM6DgguELEDEIMBEMcBEKMCOggILhDHARCjAjoOCC4QsQMQxwEQowIQkwI6CAguEMcBEK8BOgoIABCxAxCDARAKOhAILhCxAxDHARCvARAKEJMCOggIABCxAxDJAzoFCAAQkgM6BAgAEAo6BQgAEIYDUJOsJlj72CZgwegmaANwAHgAgAF4iAGSC5IBBDIwLjGYAQCgAQGqAQdnd3Mtd2l6sAEA&sclient=gws-wiz'
    driver_path = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path, options=options)
    driver.get(url)

    # Grab html xpath that stores the Name, Points Scored, and Date of the event
    name_and_points = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[3]/div/div[1]/div/div/div[1]').text
    date_of_score = driver.find_element_by_xpath(
    '/html/body/div[8]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/span[3]/span').text

    # Splits string into a name string and points string
    name_split = name_and_points.split()
    top_scorer = name_split[0] + " " + name_split[1]
    total_points = name_split[3]

    # Make statement for who the top scorer of the day was
    top_scorer_statement = top_scorer + " was the Top Scorer in the NBA today with " + total_points + " points on " + date_of_score

    guessed_right_statement = "CONGRATULATIONS! YOU GUESSED RIGHT!\n"
    guessed_wrong_statement = "WHOOPS! You Guessed Wrong! Try Again Tomorrow!\n"
    if user_guess.casefold() == top_scorer.casefold():
        label['text'] = "You guessed " + user_guess + " to be the Top Scorer in the NBA today\n" + guessed_right_statement + top_scorer_statement + "\n"
    else:
        label['text'] = "You guessed " + user_guess + " to be the Top Scorer in the NBA today\n" + guessed_wrong_statement + top_scorer_statement + "\n"


# Sets up GUI window
root = tk.Tk()
root.geometry('790x490')
root.resizable(width=0, height=0)
root.title('Guess The Top Scorer in the NBA Today')

# Sets window background as selected image
background_image = ImageTk.PhotoImage(Image.open('GuiBgImage.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# First frame to enter and submit guess
guess_frame = tk.Frame(root, bg='orange', bd=5)
guess_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# Text bar to type NBA player to guess
entry = tk.Entry(guess_frame, font=40)
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

# Button to submit guess and check to see if correct
button = tk.Button(guess_frame, text='Submit Guess', font=25, command=lambda: submit_guess(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# Bottom frame to display messages to user
main_frame = tk.Frame(root, bg='orange', bd=10)
main_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# Label from bottom frame to hold the text for all messages
label = tk.Label(main_frame, font=('Times New Roman', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()
