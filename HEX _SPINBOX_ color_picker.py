
from tkinter import *
import random

w = Tk()
w.title('HEX SPINBOX')
w.config(bg = 'magenta2')
w.geometry('625x380')
w.resizable(False, True)
w.attributes('-alpha', 0.95)

def random_HEX(r0,r1,g0,g1,b0,b1):
    pre = '#'
    color = pre + '%02x%02x%02x' % (random.randint(r0,r1), random.randint(g0,g1), random.randint(b0,b1))
    return color

def hex_color(*args):
    global t_vars, lab_var
    hex_color = '#' + ''.join( [t_vars[i].get() for i,v in enumerate(t_vars)] )
    if len(hex_color) == 7: config(hex_color)

def config(hex_color):
    w.config(bg = hex_color)
    lab.config(bg = hex_color)
    
    lab_txt_1.config(bg = hex_color, fg = random_HEX(0,255,0,255,100,255))
    lab_txt_2.config(bg = hex_color, fg = random_HEX(255,255,0,0,0,255))
    lab_txt_3.config(bg = hex_color, fg = random_HEX(0,255,0,255,0,255))
    
    lab_var.set(hex_color)



t_vars = []
spin_list = []

hex_val = range(16)
hex_rep = [str(i) for i in reversed([0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F'])]
hex_dic = dict(zip(hex_rep, hex_val))

lab_var = StringVar()
lab_var.set('')

lab_txt_1 = Label(w, text = 'THIS IS', fg = 'gray', font = ('Helvetica', '120', 'bold'))
lab_txt_1.grid(column = 0, row = 1, columnspan = 6, sticky = W)
lab_txt_2 = Label(w, text = 'HEX SPINBOX', fg = 'black', font = ('Helvetica', '60', 'bold'))
lab_txt_2.grid(column = 0, row = 2, columnspan = 6, sticky = W)
lab_txt_3 = Label(w, text = 'SETS 6 SPINBOXES TO SHOW YOU THIS VERY COLOR', fg = 'black', font = ('Helvetica', '15', 'bold'))
lab_txt_3.grid(column = 0, row = 3, columnspan = 6, sticky = W)

lab = Label(w, textvariable = lab_var, fg = '#00FFFF', font = ('Helvetica', '60', 'bold'))
lab.grid(column = 0, row = 4, columnspan = 6, sticky = W)

for i,v in enumerate(['E','E','F','F','F','3']):
    t_vars.append(StringVar())
    t_vars[i].trace('w', hex_color)
    spin_list.append(Spinbox(w, values = hex_rep, textvariable = t_vars[i], state = 'readonly', width = 10))
    spin_list[i].grid(column = i, row = 0)
    t_vars[i].set(v)

    
#t_vars = [t_vars[i].set(v) for i,v in enumerate(['6','6','F','F','F','F'])]

