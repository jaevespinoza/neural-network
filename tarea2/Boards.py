import random

from class5.NetworkCreator import NetworkCreator
from Normalizer import normalizePosition, transformToArray, normalizeComplete, transformFloat

class Board:
    def __init__(self):
        self.networkfirst = NetworkCreator().createNet(3, [9,12,9], [9, 9, 12], -3, 3, -1, 1)
        self.networksecond = NetworkCreator().createNet(3, [9, 12, 9], [9, 9, 12], -3, 3, -1, 1)
        self.entire = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]

    '''
    Checks if a row has the same elements
    '''
    def checkEqualRow(self, lst):
        return self.all_same(lst) and lst[0] != "0"


    '''
    Method to determine whether all items are the same in a list
    '''
    def all_same(self, items):
        return all(x == items[0] for x in items)


    '''
    Checks if the board is full
    '''
    def checkFull(self):
        for lst in self.entire:
            if "0" in lst:
                return False
        return True


    '''
    Returns the current status
    '''
    def getCurrentStatus(self):
         lst = []
         for rows in self.entire:
            for numbers in rows:
                lst.append(numbers)
         return lst


    '''
    Gets the diagonal rows from the board
    '''
    def getDiagonalRow(self):
        lstf = [self.entire[0][0], self.entire[1][1], self.entire[2][2]]
        lsts = [self.entire[0][2], self.entire[1][1], self.entire[2][0]]
        return [lstf, lsts]


    '''
    Gets the columns of the board
    '''
    def getColums(self):
        lstf = [self.entire[0][0],self.entire[1][0],self.entire[2][0]]
        lsts = [self.entire[0][1], self.entire[1][1], self.entire[2][1]]
        lstt = [self.entire[0][2], self.entire[1][2], self.entire[2][2]]
        return [lstf,lsts,lstt]


    '''
    Checks if any of the players has won
    '''
    def checkWin(self):
        diagonals = self.getDiagonalRow()
        columns = self.getColums()
        if self.checkEqualRow(self.entire[0]):
            print self.entire[0][0] + " won!"
            return True
        elif self.checkEqualRow(self.entire[1]):
            print self.entire[1][0] + " won!"
            return True
        elif self.checkEqualRow(self.entire[2]):
            print self.entire[2][0] + " won!"
            return True
        elif self.checkEqualRow(diagonals[0]):
            print self.entire[0][0] + " won!"
            return True
        elif self.checkEqualRow(diagonals[1]):
            print self.entire[0][2] + " won!"
            return True
        elif self.checkEqualRow(columns[0]):
            print self.entire[0][0] + " won!"
            return True
        elif self.checkEqualRow(columns[1]):
            print self.entire[0][1] + " won!"
            return True
        elif self.checkEqualRow(columns[2]):
            print self.entire[0][2] + " won!"
            return True
        else:
            return False


    '''
    Displays the current status of the board
    '''
    def display(self):
        print self.entire[0]
        print self.entire[1]
        print self.entire[2]
        print "-----------------------"


    '''
    Method that gets the current state of the board
    '''
    def getForMovement(self):
        return self.entire[0] + self.entire[1] + self.entire[2]


    '''
    Normal Tictactoe implementation
    '''
    def play(self, fsymbol, ssymbol):
        statusX = []
        movementX = []
        statusO = []
        movementO = []
        statusXn = []
        movementXn = []
        statusOn = []
        movementOn = []
        won = False
        full = False
        self.entire = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
        while not self.checkFull():


            rndX = random.randint(0, 8)
            ##rndX = input("Write input\n")
            rnds = normalizePosition(rndX)
            while self.entire[rnds[0]][rnds[1]] != "0":

                ## documentar random.randint si es que se quiere jugar computadora contra computadora
                rndX = random.randint(0, 8)
                ##rndX = input("Write input\n")
                rnds = normalizePosition(rndX)


            statusOn.append(self.getForMovement())
            statusO.append(normalizeComplete(self.getForMovement()))
            self.entire[rnds[0]][rnds[1]] = fsymbol
            movementOn.append(rndX)
            movementO.append(transformToArray(rndX))

            if self.checkWin():
                won = True
                break
            elif self.checkFull():
                full = True
                break

            rndY = random.randint(0, 8)
            #rndY = input("Write input\n")
            rndYs = normalizePosition(rndY)
            while self.entire[rndYs[0]][rndYs[1]] != "0":
                #rndY = input("Write input\n")
                rndY = random.randint(0, 8)
                rndYs = normalizePosition(rndY)
            statusX.append(normalizeComplete(self.getForMovement()))
            statusXn.append(self.getForMovement())
            self.entire[rndYs[0]][rndYs[1]] = ssymbol


            movementX.append(transformToArray(rndY))
            movementXn.append(rndY)

            if self.checkWin():
                break
            elif self.checkFull():
                full = True
                break


        if won and not full:
            self.writeToFile(statusO, movementO, "file" + fsymbol + ".txt")
            self.writeToFileNot(statusOn, movementOn, "notfile" + fsymbol + ".txt")
        elif not won and not full:
            self.writeToFile(statusX, movementX, "file" + ssymbol + ".txt")
            self.writeToFileNot(statusXn, movementXn, "notfile" + ssymbol + ".txt")
        else:
            self.writeToFile(statusO, movementO, "file" + fsymbol + ".txt")
            self.writeToFileNot(statusOn, movementOn, "notfile" + fsymbol + ".txt")
            self.writeToFile(statusX, movementX, "file" + ssymbol + ".txt")
            self.writeToFileNot(statusXn, movementXn, "notfile" + ssymbol + ".txt")

    '''
    Method that writes the status and movements normalized
    '''
    def writeToFile(self, status, movement, file):
        filea = open(file, "a")
        for i in range(len(status)):
            for j in range(len(status[i])):
                filea.write(str(status[i][j]) + " ")
            for j in range(len(movement[i])):
                filea.write(movement[i][j] + " ")
            filea.write("\n")
        filea.close()


    '''
    Method that writes the status and movements not normalized
    '''
    def writeToFileNot(self, status, movement, file):
        filea = open(file, "a")
        for i in range(len(status)):
            for j in range(len(status[i])):
                filea.write(str(status[i][j]) + " ")
            filea.write(str(movement[i]))
            filea.write("\n")
        filea.close()


    '''
    Method to play Tic Tac Toe where the neural network plays second.
    
    '''
    def playNeuralSecond(self, fsymbol, ssymbol, iterations):
        xwon = 0
        owon = 0
        draw = 0

        for i in range(iterations):
            self.entire = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
            while not self.checkFull():
                self.display()

                ##documentar si es que se quiere jugar computadora vs red

                rndX = input("Write input\n")
                #rndX = random.randint(0,8)
                rnds = normalizePosition(rndX)
                while self.entire[rnds[0]][rnds[1]] != "0":

                    rndX = input("Write input\n")

                    #rndX = random.randint(0,8)
                    rnds = normalizePosition(rndX)
                self.entire[rnds[0]][rnds[1]] = fsymbol
                self.display()

                if self.checkWin():
                    xwon += 1
                    break
                elif self.checkFull():
                    draw += 1
                    break

                board = self.getCurrentStatus()
                lst = normalizeComplete(board)
                position = self.networksecond.evaluate(lst)
                trueposition = []
                for i in range(len(board)):
                    if board[i] == "0":
                        trueposition.append(position[i])
                    else:
                        trueposition.append(0.0)
                max_val = max(trueposition)

                rndY = trueposition.index(max_val)
                rndYs = normalizePosition(rndY)
                self.entire[rndYs[0]][rndYs[1]] = ssymbol
                self.display()

                if self.checkWin():
                    owon += 1
                    break
                elif self.checkFull():
                    draw +=1
                    break
        print "Number of first wins : " + str(xwon)
        print "Number of second wins : " + str(owon)
        print "Number of draws : " + str(draw)
        return owon/1000.0

    def learn(self, symbol, epochs, net):
        for i in range(epochs):
            files = open("file" + symbol + ".txt", "r")
            filelist = files.readlines()
            for line in filelist:
                lstline = line.split(" ")
                inputs = transformFloat(lstline[0:9])
                out = transformFloat(lstline[9:18])
                net.train(inputs, out)
            files.close()

    '''
    Method to play against a Neural network where the network plays first
    
    '''
    def playNeuralFirst(self, fsymbol, ssymbol, iterations):
        firstwon = 0
        secondwon = 0
        draw = 0

        for i in range(iterations):
            self.entire = [["0", "0", "0"], ["0", "0", "0"], ["0", "0", "0"]]
            while not self.checkFull():
                self.display()
                #rndX = input("Write input\n")

                board = self.getCurrentStatus()
                lst = normalizeComplete(board)
                position = self.networkfirst.evaluate(lst)
                trueposition = []
                for i in range(len(board)):
                    if board[i] == "0":
                        trueposition.append(position[i])
                    else:
                        trueposition.append(0.0)
                max_val = max(trueposition)

                rndY = trueposition.index(max_val)
                rndYs = normalizePosition(rndY)
                self.entire[rndYs[0]][rndYs[1]] = fsymbol
                self.display()

                if self.checkWin():
                    firstwon += 1
                    break
                elif self.checkFull():
                    draw +=1
                    break

                rndX = input("Write input\n")
                #rndX = random.randint(0, 8)
                rnds = normalizePosition(rndX)
                while self.entire[rnds[0]][rnds[1]] != "0":
                    rndX = input("Write input\n")
                    #rndX = random.randint(0, 8)
                    rnds = normalizePosition(rndX)
                self.entire[rnds[0]][rnds[1]] = ssymbol
                self.display()

                if self.checkWin():
                    secondwon += 1
                    break
                elif self.checkFull():
                    draw += 1
                    break

        print "Number of first wins : " + str(firstwon)
        print "Number of second wins : " + str(secondwon)
        print "Number of draws : " + str(draw)
        return firstwon/1000.0

