from YearlyCalculation import sum_yearly
from VehicleCalculation import sum_by_vehicle
from CountryCalculation import country_sum
from PeriodCalculation import sum_period
from downloadExcel import purge, download_excel
from tkinter import *
import time
import threading
import itertools


#link of the site that is used for downloading
url = 'https://www.statistics.gr/el/statistics/-/publication/STO04/'


def main():
    
    #animation in the terminal during the downloading process of the excel files
    done = False
    def animation():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rDownloading Excel files ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\rDone!     ')

    t = threading.Thread(target=animation)
    t.start()

    
    download_excel(url)
    done = True

    #each click function for the buttons 
    def clicked1():
        sum_yearly()

    def clicked2():
        country_sum()
    
    def clicked3():
        sum_by_vehicle()

    def clicked4():
        sum_period()
    
    #creating gui for better use of the programm
    window = Tk()
    window.title("Python Project")
    window.geometry("700x600")
    window['background']='#202020'

    #creating label of the project and buttons for each of the four statistical categories
    lbl = Label(window, text="CHOOSE STATISTICAL CATEGORY", font=("Helvetica", 18), fg="#e67300", bg="#202020")
    lbl.grid(column=0, row=0)
    lbl.place(x=343, y=50, anchor="center")
    
    btn = Button(window, text="NUMBER OF TOURISTS \n YEARLY", font=("Helvetica", 12), height = 8, width = 25, bg="#e67300", fg="#202020", command=clicked1)
    btn.grid(column=1, row=1)
    btn.place(x=75, y=135)
    
    btn2 = Button(window, text="NUMBER OF TOURISTS \n BY COUNTRY", font=("Helvetica", 12), height = 8, width = 25, bg="#e67300", fg="#202020", command=clicked2)
    btn2.grid(column=1, row=1)
    btn2.place(x=390, y=135)
    
    btn3 = Button(window, text="NUMBER OF TOURISTS \n BY VEHICLE", font=("Helvetica", 12), height = 8, width = 25, bg="#e67300", fg="#202020", command=clicked3)
    btn3.grid(column=1, row=1)
    btn3.place(x=75, y=350)
    
    btn4 = Button(window, text="NUMBER OF TOURISTS \n EVERY 3 MONTHS", font=("Helvetica", 12), height = 8, width = 25, bg="#e67300", fg="#202020", command=clicked4)
    btn4.grid(column=1, row=1)
    btn4.place(x=390, y=350)
    window.mainloop()

    #erases all the excel files for less storage use
    purge()

main()