from pysvg.builders import *
import random


def cirZero(canvas, builder, row, col):
    canvas.addElement(pathZeroTop(row, col, 0.15))
    canvas.addElement(pathZeroBot(row, col, 0.15))


def cirOne(canvas, builder, row, col):
    canvas.addElement(pathOneTop(row, col, 0.15))
    canvas.addElement(pathOneBot(row, col, 0.15))


#<path d="m 0.5  0 a 0.5  0.5  0  0  1  -.5  .5 " style="fill:none; stroke-width:0.15; stroke:black; "  />
#<path d="m .5  1 a 0.5  0.5  0  0  1  .5  -.5 " style="fill:none; stroke-width:0.15; stroke:black; "  />


def pathZeroTop(x, y, strokewidth):
    p = Path()
    p.appendMoveToPath(x + 0.5, y)
    p.appendArcToPath(.5, .5, -0.5, 0.5)

    style_dict = {'fill':"none", 'stroke-width': strokewidth, 'stroke': "black"}
    myStyle = StyleBuilder(style_dict)
    p.set_style(myStyle.getStyle())
    return p

def pathZeroBot(x, y, strokewidth):
    p = Path()
    p.appendMoveToPath(x + 0.5, y + 1)
    p.appendArcToPath(.5, .5, 0.5, -0.5)

    style_dict = {'fill':"none", 'stroke-width': strokewidth, 'stroke': "black"}
    myStyle = StyleBuilder(style_dict)
    p.set_style(myStyle.getStyle())
    return p


def pathOneTop(x, y, strokewidth):
    p = Path()
    p.appendMoveToPath(x + 1, y + 0.5)
    p.appendArcToPath(.5, .5, -0.5, -0.5)

    style_dict = {'fill':"none", 'stroke-width': strokewidth, 'stroke': "black"}
    myStyle = StyleBuilder(style_dict)
    p.set_style(myStyle.getStyle())
    return p


def pathOneBot(x, y, strokewidth):
    p = Path()
    p.appendMoveToPath(x, y + 0.5)
    p.appendArcToPath(.5, .5, 0.5, 0.5)

    style_dict = {'fill':"none", 'stroke-width': strokewidth, 'stroke': "black"}
    myStyle = StyleBuilder(style_dict)
    p.set_style(myStyle.getStyle())
    return p


def truchetArr(board):
    rowNum = 0
    dwg = Svg("dwg")
    oh = ShapeBuilder()

    for row in board:
        colNum = 0
        for col in row:
            if col:
                cirOne(dwg, oh, rowNum, colNum)
            else:
                cirZero(dwg, oh, rowNum, colNum)
            colNum += 1
        rowNum += 1

    dwg.save("circle.svg")


if __name__ == '__main__':
    rows, cols = (10, 10)
    arr = [[random.randint(0, 1) for i in range(cols)] for j in range(rows)]
    truchetArr(arr)
