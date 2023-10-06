lightField = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

for x in range(len(lightField)):
    print(lightField[x])


def hasGameEnded():
    for x in range(len(lightField)):
        for y in range(len(lightField)):
            if lightField[x][y] == 1:
                return False

    return True


def getButtonField():
    row1 = [int(x) for x in input("type in the first row (separated with spaces) \n").split()]
    row2 = [int(x) for x in input("type in the second row (separated with spaces) \n").split()]
    row3 = [int(x) for x in input("type in the third row (separated with spaces) \n").split()]

    return [row1, row2, row3]


while not hasGameEnded():
    buttonField = getButtonField()

    for i in range(len(buttonField)):
        for j in range(len(buttonField)):
            if buttonField[i][j] % 2 != 0:

                lightField[i][j] = int(not lightField[i][j])

                if i != 0:
                    lightField[i - 1][j] = int(not lightField[i - 1][j])

                if j != 0:
                    lightField[i][j - 1] = int(not lightField[i][j - 1])

                if i != 2:
                    lightField[i + 1][j] = int(not lightField[i + 1][j])

                if j != 2:
                    lightField[i][j + 1] = int(not lightField[i][j + 1])

    for x in range(len(lightField)):
        print(lightField[x])

print("Game over. You won!")
