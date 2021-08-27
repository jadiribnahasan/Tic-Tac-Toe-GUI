import tkinter as tk
import tkinter.messagebox
import copy

root = tk.Tk()
root.configure(width=600, height=800)
root.title("Tic Tac Toe")

name = tk.StringVar()
label = tk.Label(root, text="Player Name :", font='Times 20 bold',
                 fg='darkslategrey', height=1, width=12)
label.grid(row=0, column=0)
player = tk.Entry(root, textvariable=name, bd=5)
player.grid(row=0, column=1)


demolabel = tk.Label(root, text="         ")
demolabel.grid(row=1, column=0)

button1 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button1))
button1.grid(row=2, column=0)

button2 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button2))
button2.grid(row=3, column=0)

button3 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button3))
button3.grid(row=4, column=0)

button4 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button4))
button4.grid(row=2, column=1)

button5 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button5))
button5.grid(row=3, column=1)

button6 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button6))
button6.grid(row=4, column=1)

button7 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button7))
button7.grid(row=2, column=2)

button8 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button8))
button8.grid(row=3, column=2)

button9 = tk.Button(root, text=" ", font='Times 20 bold', bg='slategrey',
                    fg='gold2', height=4, width=12, command=lambda: btnClick(button9))
button9.grid(row=4, column=2)

userTurn = False


grid = [[-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]]


def btnClick(button):
    global userTurn, name
    if button["text"] == " " and userTurn == True:
        button["text"] = "X"
        if button == button1 and userTurn == True:
            grid[0][0] = 0
        elif button == button2 and userTurn == True:
            grid[1][0] = 0
        elif button == button3 and userTurn == True:
            grid[2][0] = 0
        elif button == button4 and userTurn == True:
            grid[0][1] = 0
        elif button == button5 and userTurn == True:
            grid[1][1] = 0
        elif button == button6 and userTurn == True:
            grid[2][1] = 0
        elif button == button7 and userTurn == True:
            grid[0][2] = 0
        elif button == button8 and userTurn == True:
            grid[1][2] = 0
        elif button == button9 and userTurn == True:
            grid[2][2] = 0
        userTurn = False


gridToButton = {
    '00': button1,
    '10': button2,
    '20': button3,
    '01': button4,
    '11': button5,
    '21': button6,
    '02': button7,
    '12': button8,
    '22': button9
}


buttons = [button1, button2, button3, button4,
           button5, button6, button7, button8, button9]


def isGridFull(grid):
    empty = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == -1:
                empty = empty + 1
    if empty == 0:
        return True
    else:
        return False


def isAnyoneWon(grid):
    if (grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1) or (grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1) or (grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1) or (grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1) or (grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1) or (grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1) or (grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1) or (grid[2][0] == 1 and grid[1][1] == 1 and grid[0][2] == 1):
        return 1
    elif (grid[0][0] == 0 and grid[0][1] == 0 and grid[0][2] == 0) or (grid[1][0] == 0 and grid[1][1] == 0 and grid[1][2] == 0) or (grid[2][0] == 0 and grid[2][1] == 0 and grid[2][2] == 0) or (grid[0][0] == 0 and grid[1][0] == 0 and grid[2][0] == 0) or (grid[0][1] == 0 and grid[1][1] == 0 and grid[2][1] == 0) or (grid[0][2] == 0 and grid[1][2] == 0 and grid[2][2] == 0) or (grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0) or (grid[2][0] == 0 and grid[1][1] == 0 and grid[0][2] == 0):
        return 0
    else:
        return -1


def isDraw(grid):
    if(isAnyoneWon(grid) == -1 and isGridFull(grid) == True):
        return True
    else:
        return False


def utility(grid, depth):
    if isAnyoneWon(grid) == 1:
        return 1/depth
    elif isAnyoneWon(grid) == 0:
        return -1
    else:
        return 0


def maxAlgo(grid, depth):

    if(isDraw(grid) is True or (isAnyoneWon(grid) is not -1)):
        return utility(grid, depth)

    possibleMoveOfPC = []
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == -1:
                newgrid = copy.deepcopy(grid)
                newgrid[i][j] = 1
                possibleMoveOfPC.append(newgrid)
    util = -100000.3
    for move in possibleMoveOfPC:
        util = max(util, minAlgo(move, depth+1))
    return util


def minAlgo(grid, depth):

    if(isDraw(grid) is True or (isAnyoneWon(grid) is not -1)):
        return utility(grid, depth)

    possibleMoveOfUser = []
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == -1:
                newgrid = copy.deepcopy(grid)
                newgrid[i][j] = 0
                possibleMoveOfUser.append(newgrid)
    util = 100000.3
    for move in possibleMoveOfUser:
        util = min(util, maxAlgo(move, depth+1))
    return util


def pcMove():
    possibleMove = []
    possibleMoveCount = 0
    store = []
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[i][j] == -1:
                newgrid = copy.deepcopy(grid)
                newgrid[i][j] = 1
                possibleMove.append(newgrid)
                store.append([i, j])
                possibleMoveCount = possibleMoveCount+1

    best = -100000
    index = -1
    for i in range(0, possibleMoveCount):
        util = minAlgo(possibleMove[i], depth=1)
        if util > best:
            index = i
            best = util

    grid[store[index][0]][store[index][1]] = 1
    s = f'{store[index][0]}{store[index][1]}'
    button = gridToButton[s]
    button.configure(text="O")


def userMove():
    global userTurn
    userTurn = True


def printGrid(grid):
    for x in grid:
        print(*x, sep=" ")


def mainLoop():

    if isAnyoneWon(grid) is not -1 or isDraw(grid) is True:
        if isDraw(grid) is True:
            tkinter.messagebox.showinfo("TIc Tac Toe", "Match Drawn")
        elif isAnyoneWon(grid) == 1:
            tkinter.messagebox.showinfo("Tic Tac Toe", "AI Won!")
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", f'{name.get()} Won!')
        return
    if userTurn == False:
        pcMove()
    if isAnyoneWon(grid) is not -1 or isDraw(grid) is True:
        if isDraw(grid) is True:
            tkinter.messagebox.showinfo("TIc Tac Toe", "Match Drawn")
        elif isAnyoneWon(grid) == 1:
            tkinter.messagebox.showinfo("Tic Tac Toe", "AI Won!")
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", f'{name.get()} Won!')
        return
    print("Give Move")
    userMove()
    root.after(1000, mainLoop)


userMove()
root.after(1000, mainLoop)
root.mainloop()
