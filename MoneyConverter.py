import tkinter as tk

def usd_to_idr():
    angka = textbox.get()
    dollar = float(angka)* 14242.85 
    text.set("Rp. " + str(dollar))
    label2.config(font=('Helvetica', 15, "bold"), fg="red")


window = tk.Tk()
window.title("USD TO IDR CONVERTER")
window.geometry("800x300")

label1 = tk.Label(window, text="USD", font=('Helvetica', 12, "bold"))
label1.pack()

textbox = tk.Entry(window, font=('Helvectica', 15, "bold"), justify=tk.CENTER)
textbox.pack()

btn = tk.Button(window, text="TO", command=usd_to_idr)
btn.pack()

text = tk.StringVar()
text.set("IDR")

label2 = tk.Label(window, font=('Helvetica', 12, "bold"), textvariable=text)
label2.pack()

window.mainloop()