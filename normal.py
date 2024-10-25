import builtins

jump_pressed = False
left_pressed = False
right_pressed = False

instances = []

def play():
    global jump_pressed, left_pressed, right_pressed, instances
    for xyz in range(1):
        stop = False
        if True:
            import sqclasses
            import tkinter
            from PIL import Image, ImageTk

            tk = tkinter.Toplevel()
            tk.title("Normal Mode")
            canvas = tkinter.Canvas(tk, width=800, height=600, border=0, highlightthickness=0)
            canvas.pack()
            canvas.create_rectangle(-1, -1, 801, 601, fill="#02CCFE")

            def do(oppo):
                if oppo:
                    examplegame.speed += 0.75
                    frank.speed += 0.75
                else:
                    if examplegame.speed > 0.75 and frank.speed > 0.75:
                        examplegame.speed -= 0.75
                        frank.speed -= 0.75

            up = tkinter.Button(tk, text="Speed Up (Cheat)", command= lambda: do(True))
            up.pack()
            down = tkinter.Button(tk, text="Slow Down (Cheat)", command=lambda: do(False))
            down.pack()

            examplegame = sqclasses.Game([1, 1, 1, 1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "#92664A", tkcanvas=canvas, tkmodule=tkinter, tkscreen=tk, ground="#00FF00", game_speed=5)
            # squirrel class auto-packs

            # marty 116, 97
            # rick 116, 90. USE 90 FOR RICK BECAUSE HE IS SMALL.
            # frank 116, 115


            squirrel = 'frank'

            if squirrel == 'frank':
                frank = sqclasses.Squirrel('frank', tkinter.PhotoImage(file="frankright.png", master=tk), 300, 0, 116, 115, canvas, tkinter, tk, examplegame, flipfile=tkinter.PhotoImage(file="frankleft.png", master=tk))
            elif squirrel == 'marty':
                frank = sqclasses.Squirrel('marty', tkinter.PhotoImage(file="martyright.png", master=tk), 300, 0, 116, 97,
                                           canvas, tkinter, tk, examplegame,
                                           flipfile=tkinter.PhotoImage(file="martyleft.png", master=tk))
            elif squirrel == 'rick':
                frank = sqclasses.Squirrel('rick', tkinter.PhotoImage(file="rickright.png", master=tk), 300, 0, 116, 90,
                                           canvas, tkinter, tk, examplegame,
                                           flipfile=tkinter.PhotoImage(file="rickleft.png", master=tk))
            else:
                raise NameError(ModuleNotFoundError(SyntaxError(Warning(UserWarning(EnvironmentError(SystemError("No squirrel name recognized")))))))

            frank.debug_mode = True  # Disable debug mode
            frank.pack()

            left_pressed = False
            right_pressed = False
            frank.jump_gravity(False)

            def update():
                global left_pressed, right_pressed
                if not stop:
                    print("Left:", left_pressed, "Right:", right_pressed)


                    frank.jump_gravity()


                    if left_pressed:
                        print("Attempted move left: No event")
                        frank.move_left(None)

                    if right_pressed:
                        print("Attempted move right: No event")
                        frank.move_right(None)

                    if frank.x1 > 400 and right_pressed:
                        examplegame.rects_move('left')
                    if frank.x1 < 400 and left_pressed:
                        examplegame.rects_move('right')

                    tk.after(20, update)

            def move_left(event):
                print("Left arrow key pressed")
                global left_pressed
                left_pressed = True

            def move_left_release(event):
                print("Left arrow key released")
                global left_pressed
                left_pressed = False

            def move_right(event):
                print("Right arrow key pressed")
                global right_pressed
                right_pressed = True

            def move_right_release(event):
                print("Right arrow key released")
                global right_pressed
                right_pressed = False

            def jump(event):
                print("Space key pressed, jump")
                frank.jump_gravity(True)


            tk.bind("<KeyPress-Left>", move_left)
            tk.bind("<KeyRelease-Left>", move_left_release)
            tk.bind("<KeyPress-Right>", move_right)
            tk.bind("<KeyRelease-Right>", move_right_release)
            tk.bind("<space>", jump)
            # tk.bind('<KeyPress-Down>',)

            tk.after(20, update)

            tk.mainloop()
            tk.update_idletasks()



if __name__ == "__main__":
    print("Type Play at the shell to play the game.\nIt's better to launch the main program.")
    choice = input(">>> ")
    if choice == "Play":
        play()