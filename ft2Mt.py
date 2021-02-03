from tkinter import Tk, Button, Label, DoubleVar, Entry
#creating simple GUI App
window = Tk()
window.title("Feet to Meter Conversion App")
window.configure(background="Light Green")
window.geometry("430x320")
window.resizable(width=False,height=False)

def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)
    
#for clear the value
def clear():
    ft_value.set("")
    mt_value.set("")

#Creating some Buttons ,labels etc
ft_label = Label(window,text="Feet",bg="Purple",fg="white",width=14)
ft_label.grid(column=0,row=0,padx=15,pady=15)

#Creating Some entery values
ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')

#second labels
mt_label = Label(window,text="Meter",bg="brown",fg="white",width=14)
mt_label.grid(column=0,row=1)

#Creating Some entery values
mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=25)
mt_entry.delete(0,'end')

convert_button = Button(window,text="Convert",bg="Black",fg="white",width=14,command=convert)
convert_button.grid(column=0,row=3,padx=15)

clear_button = Button(window,text="Clear",bg="Red",fg="white",width=14,command=clear)
clear_button.grid(column=1,row=3,padx=15)

window.mainloop()

