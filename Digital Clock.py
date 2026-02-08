from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%H')
    mi = time.strftime('%M')
    sec = time.strftime('%S')

    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sec)

    clock.after(200, date_time)

clock = Tk()
clock.title("LED Digital Clock")
clock.geometry("800x300")
clock.config(bg="black")

font_style = ("DS-Digital", 90, "bold")  # Use your installed digital font

lab_hr = Label(clock, text="00", font=font_style, bg="black", fg="#00FF00")
lab_hr.place(x=100, y=80)

colon1 = Label(clock, text=":", font=font_style, bg="black", fg="#00FF00")
colon1.place(x=230, y=80)

lab_min = Label(clock, text="00", font=font_style, bg="black", fg="#00FF00")
lab_min.place(x=270, y=80)

colon2 = Label(clock, text=":", font=font_style, bg="black", fg="#00FF00")
colon2.place(x=400, y=80)

lab_sec = Label(clock, text="00", font=font_style, bg="black", fg="#00FF00")
lab_sec.place(x=440, y=80)

date_time()
clock.mainloop()
