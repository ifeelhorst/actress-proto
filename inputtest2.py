import tkinter as tk
# Original: https://stackoverflow.com/questions/3501849/how-to-bind-self-events-in-tkinter-text-widget-after-it-will-binded-by-text-widge

def wert_aus_eingabe():
    print("wert 1:", entry1.get())
    print("wert 2:", entry2.get())
    print("wert 3:", entry3.get())


def button_close():
    # hier vielleicht später speichern ;-)
    gui.destroy()

def OnKeyPress(event):
    value = event.widget.get()
    string="value of %s is '%s'" % (event.widget._name, value)
    status.configure(text=string)


gui = tk.Tk()

entry1 = tk.Entry(gui, name="entry1")
entry2 = tk.Entry(gui, name="entry2")
entry3 = tk.Entry(gui, name="entry3")

# Three different bindtags. The first is just the default but I'm
# including it for illustrative purposes. The second reverses the
# order of the first two tags. The third introduces a new tag after
# the class tag.
entry1.bindtags(('.entry1', 'Entry', '.', 'all'))
entry2.bindtags(('Entry', '.entry2', '.', 'all'))
entry3.bindtags(('.entry3','Entry','post-class-bindings', '.', 'all'))

# btlabel1 = tk.Label(text="bindtags: %s" % " ".join(entry1.bindtags()))
# #tlabel2 = tk.Label(text="bindtags: %s" % " ".join(entry2.bindtags()))
# btlabel3 = tk.Label(text="bindtags: %s" % " ".join(entry3.bindtags()))
status = tk.Label(anchor="w")

entry1.grid(row=0,column=0)
# btlabel1.grid(row=0,column=1, padx=10, sticky="w")
entry2.grid(row=1,column=0)
# btlabel2.grid(row=1,column=1, padx=10, sticky="w")
entry3.grid(row=2,column=0)
# btlabel3.grid(row=2,column=1, padx=10)
status.grid(row=3, columnspan=2, sticky="w")

# normally you bind to the widget; in the third case we're binding
# to the new bindtag we've created
entry1.bind("<KeyPress>", OnKeyPress)
entry2.bind("<KeyPress>", OnKeyPress)
entry3.bind_class("post-class-bindings", "<KeyPress>", OnKeyPress)

button = tk.Button(gui, text="Speichern", command=wert_aus_eingabe)
button.grid(row = 4, columnspan = 2, pady=10)

btn_close = tk.Button(gui, text="Ende", command=button_close)
btn_close.grid(row = 5, columnspan = 2, pady=10)

gui.mainloop()
