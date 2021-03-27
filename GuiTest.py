import tkinter as tk
from PIL import Image, ImageTk

HEIGHT = 490
WIDTH = 790


def submit_guess(entry):
    label['text'] = "You guessed " + entry + " would be the Top Scorer in the NBA today"


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('GuiBgImage.jpg'))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='orange', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text='Submit Guess', font=25, command=lambda: submit_guess(entry.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

main_frame = tk.Frame(root, bg='orange', bd=10)
main_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(main_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
