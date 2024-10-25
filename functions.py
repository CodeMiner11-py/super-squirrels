def RectangularCollision(x1, y1, x2, y2, rx1, ry1, rx2, ry2):
    return not (x2 <= rx1 or x1 >= rx2 or y2 <= ry1 or y1 >= ry2)

if __name__ == '__main__':
    print("This is just a file for functions.")