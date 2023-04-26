import time
import pyglet
import random
display = pyglet.canvas.Display()
screen = display.get_default_screen()
screen_width = screen.width
screen_height = screen.height

window = pyglet.window.Window(
    width=int(screen_width * 0.9), height=int(screen_height*0.9))

initialPoints = []
points = []
pointObjects = []
pointBatch = pyglet.graphics.Batch()

numpoints = 3
pointCount = [0, 0, 0]

print('Left click to add 4 points, once added, left click for 100 iterations, right click for 1000 iterations, middle click for 10000 iterations\n')


def nextPoint():
    randomPointIndex = random.randint(0, numpoints-1)
    match randomPointIndex:
        case 0:
            pointCount[0] += 1
        case 1:
            pointCount[1] += 1
        case 2:
            pointCount[2] += 1
    randomPoint = initialPoints[randomPointIndex]
    currentPoint = points[-1]
    x = (randomPoint[0] + currentPoint[0])/2
    y = (randomPoint[1] + currentPoint[1])/2
    x2 = (x + currentPoint[0])/2
    y2 = (y + currentPoint[1])/2
    points.append((x, y))
    pointObjects.append(pyglet.shapes.Circle(x=x, y=y, radius=1, color=(
        0, 0, 255), batch=pointBatch))

    return (x, y)


@window.event
def on_draw():
    window.clear()
    pointBatch.draw()


@window.event
def on_mouse_press(x, y, button, modifiers):
    if len(points) < numpoints+1:
        if len(points) < numpoints:
            initialPoints.append((x, y))
        points.append((x, y))
        pointObjects.append(pyglet.shapes.Circle(x=x, y=y, radius=1, color=(
            0, 0, 255), batch=pointBatch))
    else:
        match button:
            case pyglet.window.mouse.LEFT:
                it = 100
            case pyglet.window.mouse.RIGHT:
                it = 1000
            case pyglet.window.mouse.MIDDLE:
                it = 10000
        for _ in range(it):
            nextPoint()
        for inx, count in enumerate(pointCount):
            string = "Point " + \
                str(inx) + " distribution: " + \
                str(count/len(points)*100)[0:5] + "%"
            print(string)
        print('\n')


pyglet.app.run()
