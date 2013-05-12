from tkinter import *
from tkinter import ttk
root = Tk()

import random

h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=1, row=1, sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=1, sticky=(W,E))
v.grid(column=1, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y


def krug(event):
    new_window = Tk()
    text1 = Label(new_window, text = 'Радиус', width = 10, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 0, column = 0, sticky ='nw' )
    scale_w = Scale(new_window, orient = HORIZONTAL, length = 500, from_ = 0, to = 1000, tickinterval = 100, resolution = 1)
    scale_w.grid(row = 0, column = 2,columnspan = 5, sticky ='nw')
    text2 = Label(new_window, text = 'Центр окружности', width = 20, height = 1, fg = 'black', font = 'arial 10')
    text2.grid(row = 1, column = 0, sticky ='nw' )
    text1 = Label(new_window, text = 'x:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 1, column = 1, sticky ='nw' )
    koord_x = Scale(new_window, orient = HORIZONTAL, length = 250, from_ = 0, to = 500, tickinterval = 100, resolution = 1)
    koord_x.grid(row = 1, column = 2, sticky ='nw' )
    text1 = Label(new_window, text = 'y:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 1, column = 3, sticky ='nw' )
    koord_y = Scale(new_window, orient = HORIZONTAL, length = 250, from_ = 0, to = 500, tickinterval = 100, resolution = 1)
    koord_y.grid(row = 1, column = 4, sticky ='nw' )
    
    def getVal(new_window):
        rad = scale_w.get()
        x = koord_x.get()
        y = koord_y.get()
        krug = canvas.create_oval((x,y,x+rad,y+rad),fill = color, tag = 'oval' )
        
        
    button_ok = Button(new_window, text = 'Выполнить', width = 10, height = 2, fg = 'black', command = new_window.destroy)
    button_ok.grid(row = 3, column = 6,sticky ='se' )
    button_ok.bind('<Button-1>', getVal)
    new_window.mainloop()


def kvadrat(event):
    new_window = Tk()
    text2 = Label(new_window, text = 'угловыe точки', width = 20, height = 1, fg = 'black', font = 'arial 10')
    text2.grid(row = 0, column = 5, sticky ='nw' )
    text2 = Label(new_window, text = 'верхняя левая', width = 20, height = 1, fg = 'black', font = 'arial 10')
    text2.grid(row = 1, column = 0, sticky ='nw' )
    text1 = Label(new_window, text = 'x:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 1, column = 3, sticky ='nw' )
    koord_x1 = Scale(new_window, orient = HORIZONTAL, length = 200, from_ = 0, to = 400, tickinterval = 100, resolution = 1)
    koord_x1.grid(row = 1, column = 4, sticky ='nw' )
    text1 = Label(new_window, text = 'y:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 1, column = 7, sticky ='nw' )
    koord_y1 = Scale(new_window, orient = HORIZONTAL, length = 200, from_ = 0, to = 400, tickinterval = 100, resolution = 1)
    koord_y1.grid(row = 1, column = 8, sticky ='nw' )
    text2 = Label(new_window, text = 'нижняя правая', width = 20, height = 1, fg = 'black', font = 'arial 10')
    text2.grid(row = 2, column = 0, sticky ='nw' )
    text1 = Label(new_window, text = 'x:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 2, column = 3, sticky ='nw' )
    koord_x2 = Scale(new_window, orient = HORIZONTAL, length = 200, from_ = 0, to = 400, tickinterval = 100, resolution = 1)
    koord_x2.grid(row = 2, column = 4, sticky ='nw' )
    text1 = Label(new_window, text = 'y:', width = 2, height = 1, fg = 'black', font = 'arial 10')
    text1.grid(row = 2, column = 7, sticky ='nw' )
    koord_y2 = Scale(new_window, orient = HORIZONTAL, length = 200, from_ = 0, to = 400, tickinterval = 100, resolution = 1)
    koord_y2.grid(row = 2, column = 8, sticky ='nw' )
    
    def getVal(new_window):
        x1 = koord_x1.get()
        x2 = koord_x2.get()
        y1 = koord_y1.get()
        y2 = koord_y2.get()
        krug = canvas.create_rectangle((x1,y1,x2,y2),fill = color, tag = "rect" )
        
        
    button_ok = Button(new_window, text = 'Выполнить', width = 10, height = 2, fg = 'black', command = new_window.destroy)
    button_ok.grid(row = 3, column = 8,sticky ='se' )
    button_ok.bind('<Button-1>', getVal)
    new_window.mainloop()
    
    
    
def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)


canvas.bind("<Button-1>",xy )
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

colors = ['black', 'white', 'red', 'green', 'yellow', 'brown']


id = canvas.create_rectangle((10, 10, 20, 30), fill="red", tags=('palette', 'palettered'))
line = canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
id = canvas.create_rectangle((10, 35, 20, 55), fill="blue", tags=('palette', 'paletteblue'))
line = canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
id = canvas.create_rectangle((10, 85, 20, 105), fill="grey", tags=('palette', 'palettegrey'))
line = canvas.tag_bind(id, "<Button-1>", lambda x: setColor("grey"))
id = canvas.create_rectangle((10, 60, 20, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
line = canvas.tag_bind(id, "<Button-1>",lambda x: setColor("black"))
id = canvas.create_oval((10,110,30,130), fill = "white", tags=('palette', 'palettepink'))
canvas.tag_bind(id, "<Double-Button-1>", krug)
id = canvas.create_rectangle((10,135,30,155), fill = "white", tags=('palette', 'palettepink'))
canvas.tag_bind(id, "<Double-Button-1>", kvadrat)
def clearCanvas(event):
    canvas.delete("rect")
    canvas.delete("tag_bind")
    canvas.delete(line)
    
canvas.bind("<Button-3>", clearCanvas)


setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop()
