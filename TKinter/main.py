import tkinter

window = tkinter.Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.pack()


def button_clicked():
    print("I got clicked")
    new_text = answer.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

answer = tkinter.Entry(width=10)
answer.pack()

window.mainloop()
