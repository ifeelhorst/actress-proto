import sqlite3
import csv
import tkinter as tk
from tkinter import filedialog

# GUI Prototyping
gui = tk.Tk()
gui.geometry("450x600")
gui.title("Schauspielerinnen")

# Datenbank
database = sqlite3.connect("actress.db")
__DATEI = ("actress.csv")
cursor = database.cursor()

actressList = []
actressListDB = []

### ------------------ Buttons
def button_open_file():

   file = filedialog.askopenfile(mode='r', filetypes=[('CSV Files', '*.csv')])
   datei_auslesen(file.name)
   if file:
      content = file.read()
      file.close()
      # print("%d characters in this file" % len(content))


def button_close():
    # hier vielleicht später speichern ;-)
    gui.destroy()

### ------------------ Datenbank-Handling
def db_table_create():
    """legt die Tabelle an; achtet darauf, dass diese nur einmal vorkommt. Kann also immer aufgerufen werden """
    cursor.execute("CREATE TABLE IF NOT EXISTS actress (vorname varchar, nachname varchar, gebdatum date)")


def db_auslesen():
    for row in cursor.execute('SELECT * FROM actress ORDER BY vorname ASC'):
        actressListDB.append(row)

def show_actress():
    i = 1
    for row in actressListDB:

        label0 = tk.Label(gui, text=row[0] ) # bg="lightblue"
        label1 = tk.Label(gui, text=row[1] )
        label2 = tk.Label(gui, text=row[2] )
        inputField = tk.Entry(gui, textvariable="")

        label0.grid(row = i, column = 0)
        label1.grid(row = i, column = 1)
        label2.grid(row = i, column = 2)
        inputField.grid(row = i, column = 3)

        i += 1
        # label = tk.Label(gui, text=row[0]+" "+row[1] ) # bg="lightblue"
        # label.pack()

def db_changes():
    """Schreibt, wieviele Daten-Änderungen es in der Tabelle gab"""
    tk.Label(gui, text="Änderungen in diesem Lauf: "+str(database.total_changes), fg="grey", height="2").pack()

### ------------------ ???
def check_duplicates_and_save():
    for i in actressListDB:
        for y in actressList:
            if i[0]==y[0]:
                actressList.remove(y)
    #print(actressList)
    cursor.executemany("""
                INSERT INTO actress
                        VALUES (?,?,?)
                """, actressList)
    database.commit()
    gui.update()
    db_changes()

### ------------------ Datei-Handling
def datei_auslesen(datei=__DATEI):
    """liest eine CSV-Datei aus und fügt diese an die Liste an"""
    with open(datei, encoding="ISO8859", newline='') as csvdatei:
        actress = csv.reader(csvdatei, delimiter=';')
        i = 0
        for row in actress:
            if i > 0:
                 actressList.append(row)
            i = i+1
        # herausfiltern unnützer items (Spalten) aus Datei-Import
        for item in actressList:
            del item[0]

        check_duplicates_and_save()



### ------------------ Test-Methoden
def testdaten_lesen_aus_datei(datei=__DATEI):
    """TEST-Methode init aus datei"""
    with open(datei, encoding="ISO8859", newline='') as csvdatei:
        actress = csv.reader(csvdatei, delimiter=';')
        i = 0
        for row in actress:
            if i > 0:
                 actressList.append(row)
            i = i+1
    print(actressList)


def testdaten_schreiben():
    """TEST-Methode init von daten in SQLITE inkl. Auslesen"""
    with open('actress.csv', encoding="ISO8859", newline='') as csvdatei:
        actress = csv.reader(csvdatei, delimiter=';')
        i = 0
        for row in actress:
            if i > 0 :
                cursor.execute('INSERT INTO actress (vorname, nachname, gebdatum) VALUES (?, ?, ?)', (row[1], row[2], row[3]) )
            i = i+1
        database.commit()
        db_changes()

### ------------------ MAINLOOP
def main():
    db_table_create()
    # testdaten_schreiben()
    db_auslesen()
    show_actress()
    btn1 = tk.Button(gui, text="Browse", command=button_open_file)
    btn3 = tk.Button(gui, text="Save", command=button_open_file)
    btn2 = tk.Button(gui, text="Schließen", command=button_close)
    btn1.grid(row = 0, column=0)
    btn3.grid(row = 0, column=1)
    btn2.grid(row = 0, column=2, columnspan=2, sticky='e', pady=10, padx=10)

if __name__ == "__main__":
    main()
    # testdaten_lesen_aus_datei()
    gui.mainloop()  #display
