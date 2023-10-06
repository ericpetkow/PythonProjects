width = 5
height = 7

BoolList = [False, False, False, False, False,
            False, False, False, False, False,
            True, True, True, True, False,
            False, False, False, False, False,
            False, True, True, True, True,
            False, False, False, False, False,
            True, False, True, False, True]

RowList = list()  # List with Bools of every row -> 2D List
for i in range(0, len(BoolList), width):
    RowList.append(BoolList[i: i + width])

NextList = []  # List with Bools and Nexts where row ends or is skipped -> 2D List either Bools or Next

whiteLine = True
for j in range(height):
    for k in range(width):
        if RowList[j][k]:
            whiteLine = False
            break

    if whiteLine:
        NextList.append("next")
    else:
        NextList.append(RowList[j])
        NextList.append("next")

    whiteLine = True

reversebool = False
for l in range(1, len(NextList)):
    if NextList[l] == "next":
        continue
    if reversebool:
        NextList[l].reverse()

    reversebool = not reversebool


StepList = []  # list with steps in each row until pen down and with nexts
for x in range(len(NextList)):
    stepCounter = 0
    if NextList[x] == "next":
        StepList.append("next")
        continue
    appendedList = []  # necessary to get all steps in one row in on list
    for y in range(width):
        if NextList[x][y]:
            appendedList.append(stepCounter)
            stepCounter = 1
        else:
            stepCounter += 1
    StepList.append(appendedList)


rightDirection = True
placeholder = None  # necessary to know if previous element in StepList was 'next'

for m in StepList:
    # if m == "next"
    #   Motory.run_angle(-1000, Winkely
    # else
    #   for x in m
    #       if dir
    #           Motorx.run_angle(1000, Winkelx * x)
    #           Motorz.run_angle(1000, 360
    #
    #       else
    #           Motorx.run_angle(-1000, Winkelx * x
    #           Motorz.run_angle(1000, 360
    if m == "next" and placeholder != "next" and placeholder is not None:
        rightDirection = not rightDirection  # reverses direction
    placeholder = m
