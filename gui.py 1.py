import tkinter

window = tkinter .Tk()

window.title("qweasdzxc")
window.geometry("640x400+100+100")
window.resizable(False,False)

def btnClick():
    label.config(font=("Arial", 40))
    label.config(text=("안산공업고등학교 컴퓨터과"))
    label.config(fg="red")

label = tkinter.Label(window, text = "안산공업고등학교")
label.pack()                         

button = tkinter.Button(window, text="확인", command=btnClick)
button.pack()

window.mainloop()
