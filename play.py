import tkinter
homewindow = tkinter.Tk()
homewindow.wm_deiconify()
homewindow.title("Home Page")

def normal_mode():
    import normal
    normal.play()



play_button = tkinter.Button(homewindow, text="Normal Mode", command=normal_mode)
play_button.pack(pady=100, padx=100)

homewindow.mainloop()
