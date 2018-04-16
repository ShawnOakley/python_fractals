
import turtle

def make_fractal(length, langle, rangle, iterations, axiom, target, replace, target2, replace2):

    state = axiom
    turtle.speed(0)
    for i in range(iterations):
        nextState=''
        for character in state:
            if character == target:
                nextState += replace
            elif character == target2:
                nextState += replace2
            else:
                nextState += character
        state = nextState

    turtle.down()
    turtle.color('red', 'black')
    turtle.begin_fill()

    for move in state:
        if move == 'F':
            turtle.forward(length)
        elif move == 'R':
            turtle.right(rangle)
        elif move == 'L':
            turtle.left(langle)

if __name__ == '__main__':
    iterations = int(input('Enter the number of generations: '));
    myLen = int(input("Enter the forward movement length: "));
    make_fractal(myLen, 90, 90, iterations, 'FX','X', 'XRYFR', 'Y','LFXLY')
