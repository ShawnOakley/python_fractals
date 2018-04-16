
import turtle

def serpinski(side, level):
    angle=60

    if level == 0:
        for i in range(3):
            t.fd(side)
            t.left(180-angle)
    else:
        serpinski(side/2, level-1)
        t.fd(side/2)
        serpinski(side/2, level-1)
        t.bk(side/2)
        t.left(angle)
        t.fd(side/2)
        t.right(angle)
        serpinski(side/2, level-1)
        t.left(angle)
        t.bk(side/2)
        t.right(angle)

if __name__ == '__main__':
    iterations = int(input('Enter the number of generations: '));
    myLen = int(input("Enter the forward movement length: "));
    t = turtle.Turtle();
    t.speed(0)
    t.shape('turtle')
    t.up()
    t.setpos(-myLen/2, -myLen/2)
    t.down()
    t.color('black','black')
    t.begin_fill()
    serpinski(myLen, iterations)
    t.end_fill()
