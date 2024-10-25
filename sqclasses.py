import functions

# class for frank and his buddies
class Squirrel:
    def __init__(self, name, imagefile, x, y, width, height, canvasname, tkmodule, tkscreen, game, flipfile):
        self.image = imagefile
        self.flip_file = flipfile
        self.current_image = self.flip_file
        self.x1, self.y1 = x, y
        self.name = name
        self.width, self.height = width, height
        self.canvas = canvasname
        self.tkmodule = tkmodule
        self.screen = tkscreen
        self.state = "grounded"
        self.image_storage = [self.image, self.flip_file]
        self.gravity = 0
        self.deleted = False
        self.id = None
        self.rects = game.rectangles
        self.rect_coords = game.rect_coords
        self.speed = 5  # Horizontal movement speed
        self.direction = 1
        self.on_ground = (False, None)
        self.right_side = list()
        self.left_side = list()
        self.debug_mode = True
        self.x2 = x+width
        self.first_time_pack = True
        self.y2 = y+height
        self.groundCheck()
        self.game = (game, False, False) # (connected game (Game class), error string, connected true/false)
        self.game[0].pack()
        self.game_obj = self.game[0]

    def update_sides(self):
        self.right_side = list() # empty lists
        self.left_side = list()
        right_x = self.x1 + self.width
        left_x = self.x1
        start = self.y1 + 1 # AVOID THE POINTS!!!
        end = self.y1 + self.height # don't avoid here, because range() will auto-avoid

        for side_y in range(int(start)+10, int(end)-35):
            self.right_side.append([right_x, side_y])
            self.left_side.append([left_x, side_y])

    def pack(self):
        if not self.debug_mode:
            print("Debug mode is off for Squirrel "+self.name)
        else:
            print("Debug mode is on for Squirrel "+self.name)
            if self.first_time_pack:
                print("coords " + str(self.rect_coords) + ", rects " + str(self.rects))
                self.first_time_pack = False
        self.current_image = self.image if self.direction == 1 else self.flip_file
        self.id = self.canvas.create_image(self.x1, self.y1, image=self.current_image, anchor="nw")
        self.update_sides()

    def groundCheck(self):
        on_ground = False
        for rect in self.rect_coords:
            if functions.RectangularCollision(self.x1, self.y1, self.x1 + self.width, self.y1 + self.height, rect[0],
                                              rect[1], rect[2], rect[3]):
                self.on_ground = (True, rect)
                on_ground = True
                break
        if not on_ground:
            self.on_ground = (False, None)
        # #if self.y2 > int(self.canvas.winfo_height()):
        # #    self.delete_squirrel()

    def update_squirrel(self, change=False, change_to=0):
        self.update_sides()
        self.groundCheck()
        if change:
            self.canvas.coords(self.id, 5000, 5000)
            if change_to == 2:
                self.current_image = self.flip_file
                self.pack()
                self.direction = 2
            elif change_to == 1:
                self.current_image = self.image
                self.pack()
                self.direction = 1
        self.canvas.coords(self.id, self.x1, self.y1)

    def check_basic_coll(self):
        if self.debug_mode:
            on_ground = False
            for rect in self.rect_coords:
                touching = functions.RectangularCollision(self.x1, self.y1, self.x1 + self.width, self.y1 + self.height,
                                                          rect[0], rect[1], rect[2], rect[3])
                if touching:
                    if self.debug_mode:
                        print(f"Collision detected with rectangle: {rect}")
                        self.on_ground = (True, rect)
                    self.state = "grounded"
                    self.gravity = 0
                    on_ground = True
                    break
            if on_ground:
                print("TOUCHING A RECTANGLE.")
                return True
            else:
                print("NOT TOUCHING A RECTANGLE")
                return False
    def jump_gravity(self, jump=False):
        self.rect_coords = self.game[0].rect_coords
        self.update_sides()
        self.groundCheck()
        check = self.check_basic_coll()
        self.current_image = self.image if self.direction == 1 else self.flip_file


        # finds out if squirrel is sinking for some reason in quicksand (DELETED FEATURE. FALLING FIXED)
        ##for rect in self.rects:
        #    #for point in ((self.x1, self.y2), (self.x2, self.y1)):
        #        #if point[0] > rect[0] and point[1] > rect[1] + 2 and point[0] < rect[3]:
        #            #self.y1 = rect[1] - self.height
        #            #if self.debug_mode:
        #                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSinking stopped!")

        if not self.deleted:
            if self.debug_mode:
                print("State is "+self.state+"\nOn Ground: "+str(self.on_ground))
                print("Direction of squirrel is "+str(self.direction))
                # #print("coords "+str(self.rect_coords)+", rects "+str(self.rects))
            self.groundCheck()
            if self.state == "grounded" and not self.on_ground[0]:
                if self.debug_mode:
                    print("Squirrel police has detected illegal flying")
                self.state = "falling"
            if self.state == "grounded" and jump: # if it is not jumping and it wants to jump
                self.state = "jumping"
                self.gravity = 10
            if self.state == "jumping":
                self.on_ground = (False, None)
                self.gravity -= 0.25
                self.y1 -= self.gravity/1.25
                if self.gravity <= 0:
                    if self.debug_mode:
                        print("Jumping has finished and now falling.")
                    self.state = "falling"
                    self.gravity = 0

            if self.state == "falling":
                self.gravity += 0.25
                self.y1 += self.gravity/1.25
                for rect in self.rect_coords:
                    touching = functions.RectangularCollision(self.x1, self.y1, self.x1 + self.width, self.y1 + self.height, rect[0], rect[1], rect[2], rect[3])
                    if touching:
                        if self.debug_mode:
                            print(f"Collision detected with rectangle: {rect}")
                            self.on_ground = (True, rect)
                        self.state = "grounded"
                        self.gravity = 0
                        self.on_ground = (True, rect)
                        break
                    if not touching:
                        self.on_ground = (False, None)
            self.update_squirrel()
            if self.state != "grounded":
                self.screen.after(int((-(10*self.speed))+120), self.jump_gravity)

    def move_left(self, event, actually_move=True, flip=True):
        if self.debug_mode:
            print("Squirrel "+self.name+" is trying to move left.")
        if not self.deleted and not self.x1 < 2:
            touching = False
            if self.on_ground:
                touching = False
                for lpt in self.left_side:
                    for rect in self.rect_coords:
                        touching = functions.RectangularCollision(lpt[0] - 10, lpt[1], lpt[0], lpt[1], rect[0], rect[1],
                                                                  rect[2], rect[3])
                        if touching:
                            if self.debug_mode:
                                print(f"Left side collision @ {lpt} with rect {rect}")
                            self.x1 += self.speed*2.5
                            break
                    if touching:
                        break

                if not touching:
                    if actually_move:
                        self.x1 -= self.speed
                    if self.debug_mode:
                        print("Squirrel "+self.name+" is successful in moving left.")
                    self.update_squirrel()
                    for rect in self.rect_coords:
                        touching = functions.RectangularCollision(self.x1, self.y1, self.x1 + self.width,
                                                                  self.y1 + self.height, rect[0], rect[1], rect[2],
                                                                  rect[3])
                        if touching:
                            if self.debug_mode:
                                print(f"Left side collision detected at point with rectangle: {rect}")
                            self.state = "grounded"
                            self.gravity = 0
                            break
                    else:
                        self.on_ground = (False, None)
                        self.state = "falling"

                    if flip:
                        self.update_squirrel(change=True, change_to=2)

            elif self.debug_mode:
                print("Moving Left. Touching.")
            return touching

    def move_right(self, event, actually_move=True, flip=True):
        if self.debug_mode:
            print("Squirrel "+self.name+" is trying to move right.")
        if not self.deleted and not self.x1 + self.width > 800:
            touching = False
            if self.on_ground:
                touching = False
                for rpt in self.right_side:
                    for rect in self.rect_coords:
                        touching = functions.RectangularCollision(rpt[0], rpt[1], rpt[0] + 10, rpt[1], rect[0], rect[1],
                                                                  rect[2], rect[3])
                        if touching:
                            self.x1 -= self.speed*2.5
                            if self.debug_mode:
                                print(f"Right side collision detected at point {rpt} with rectangle {rect}")
                            break
                    if touching:
                        break

                if not touching:
                    if actually_move:
                        self.x1 += self.speed
                    if self.debug_mode:
                        print("Squirrel "+self.name+" is successful in moving right.")
                    self.update_squirrel()
                    for rect in self.rect_coords:
                        touching = functions.RectangularCollision(self.x1, self.y1, self.x1 + self.width,
                                                                  self.y1 + self.height, rect[0], rect[1], rect[2],
                                                                  rect[3])
                        if touching:
                            if self.debug_mode:
                                print(f"MOVE RIGHT Collision detected with rectangle: {rect}")
                            self.state = "grounded"
                            self.gravity = 0
                            break
                    else:
                        self.on_ground = (False, None)
                        self.state = "falling"

                    if flip:
                        self.update_squirrel(change=True, change_to=1)

            return touching

    def delete_squirrel(self):
        self.canvas.coords(self.id, 5000, 5000)
        self.deleted = True
        if self.debug_mode:
            print(("SYSTEM DELETE SQUIRREL "+self.name.upper()+" \n") * 10)


class Game:
    def __init__(self, gamelist, color, tkcanvas, tkmodule, tkscreen, ground=True, game_speed=1):
        if ground == True:
            self.ground_color = color
        else:
            self.ground_color = ground
        self.gamelist = gamelist
        self.newlist = [int(x) * 75 for x in self.gamelist]
        self.color = color
        self.rectangles = []
        self.rect_coords = []
        self.screen = tkscreen
        self.module = tkmodule
        self.canvas = tkcanvas
        self.moving = False
        self.speed = game_speed



    def update_rect(self):
        counter = 0
        self.canvas.create_rectangle(0, 500, 800, 600, fill=self.ground_color, outline="#000", width=10)
        for height in self.newlist:
            x1, y1 = (counter * 75, 500)
            x2, y2 = (x1 + 75, 500 - height)
            rect = self.canvas.create_rectangle(x1, y2, x2, y1, fill=self.color, outline="#000", width=10)  # Note y2 and y1 are swapped
            self.rectangles.append(rect)
            self.rect_coords.append((x1, y2, x2, y1))  # Note y2 and y1 are swapped
            counter += 1

    def update_coords(self):
        self.rect_coords = []
        for rect in self.rectangles:
            self.rect_coords.append(self.canvas.coords(rect))

    def rects_move(self, direction):
        direction_x = (-self.speed if direction == 'left' else self.speed if direction == 'right' else 0)
        for rect in self.rectangles:
            self.canvas.move(rect, direction_x, 0)
        self.update_coords()


    def pack(self):
        self.update_rect()
        return self

if __name__ == '__main__':
    print("This is just a file for classes.")