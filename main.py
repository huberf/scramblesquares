#'A' = pink
#'B' = black
#'C' = 'white'
#'D' = green
# 0 is heads
# 1 is tails
import json

dataFile = open('cards.json')
data = dataFile.read()
cards = json.loads(data)

gameBoard = [
        [None, None, None],
        [None,None,None],
        [None,None,None]
        ]

def check(game, x, y, xOffset, yOffset):
    a = 0
    b = 0
    if xOffset != 0:
        if xOffset == -1:
            a = 3
            b = 1
        else:
            a = 1
            b = 3
    else :
        if yOffset == -1:
            a = 0
            b = 2
        else:
            a = 2
            b = 0
    if game[y+yOffset][x+xOffset][b][0] == game[y][x][a][0] and game[y+yOffset][x+xOffset][b][1] != game[y][x][a][1]:
        return True
    else:
        return False

def getMatchCoordinatesRight(right, left):
    coordinates = []
    for i in range(4):
        for a in range(4):
            if right[i][0] == left[a][0] and right[i][1] != left[a][1]:
                coordinates += [[i, a]]
    return coordinates

def getMatchCoordinatesBottom(bottom, top):
    coordinates = []
    for i in range(4):
        for a in range(4):
            if bottom[i][0] == top[a][0] and bottom[i][1] != top[a][1]:
                coordinates += [[i, a]]
    return coordinates


def test(game):
    for i in range(3):
        for a in range(3):
            if not i == 0:
                if not check(game, i, a, 0, -1):
                    return False
            if not i == 2:
                if not check(game, i, a, 0, 1):
                    return False
            if not a == 0:
                if not check(game, i, a, -1, 0):
                    return False
            if not a == 2:
                if not check(game, i, a, 1, 0):
                    return False
    return True

def generate(gameBoards, usedCards, usedA, x, y):
    for i in range(len|(cards)):
        for a in range(4):
            points = [a, a+1, a+2, a+3]
            for z in range(4):
                if points[z] == 4:
                    points[z] = 0
                elif points[z] == 5:
                    points[z] = 1
                elif points[z] == 6:
                    points[z] = 2
                elif points[z] == 7:
                    points[z] = 3
            gameBoard[x][y] = [cards[i][points[0]], cards[i][points[1]], cards[i][points[2]], cards[i][points[3]]]
            if not y == 2 and x == 2:
                if x == 2:
                    x = 0
                    y = y+1
                else:
                    x = x + 1
                generate(usedCards, usedA, x, y)
            else:
                print("Finished generation")

'''
generate(
    {},
    {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []},
    0,
    0
)
'''

def normalize(points):
    for z in range(4):
        if points[z] == 4:
            points[z] = 0
        elif points[z] == 5:
            points[z] = 1
        elif points[z] == 6:
            points[z] = 2
        elif points[z] == 7:
            points[z] = 3
    return points

vals = [0,1,2,3]
def start(game):
    gameBoards = []
    for i in range(4*4*4*4*4*4*4*4*4*9):
        gameBoards += []
    for a in range(len(game)):
        for i0 in vals:
            points0 = normalize([i0, i0+1, i0+2, i0+3])
            for i1 in vals:
                points1 = normalize([i1, i1+1, i1+2, i1+3])
                check([[]])
                for i2 in vals:
                    points2 = normalize([i2, i2+1, i2+2, i2+3])
                    for i3 in vals:
                        points3 = normalize([i3, i3+1, i3+2, i3+3])
                        for i4 in vals:
                            for i5 in vals:
                                for i6 in vals:
                                    for i7 in vals:
                                        points1 = [i, i+1, i+2, i+3]
                                        for z in range(4):
                                            if points[z] == 4:
                                                points[z] = 0
                                            elif points[z] == 5:
                                                points[z] = 1
                                            elif points[z] == 6:
                                                points[z] = 2
                                            elif points[z] == 7:
                                                points[z] = 3
            tempBoard = [
                [None, None, None],
                [None,None,None],
                [None,None,None]
            ]
            points = [i, i+1, i+2, i+3]
            for z in range(4):
                if points[z] == 4:
                    points[z] = 0
                elif points[z] == 5:
                    points[z] = 1
                elif points[z] == 6:
                    points[z] = 2
                elif points[z] == 7:
                    points[z] = 3
            coordinates = []
            for z in range(65536):
                gameBoards[i*z*a] = [
                    [[cards[game[a]][points[0]], cards[game[a]][points[1]], cards[game[a]][points[2]], cards[game[a]][points[3]]], None, None],
                    [None, None, None],
                    [None, None, None]
                ]
            gameBoards[i*z*a]
    usedCards[str(i)] = True
    usedA = {"1": [0, 1, 2, 3], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": []}
    generate(gameBoards, usedCards, usedA, 0, 1)

sequenceFile = open('sequences.json')
allSequences = json.loads(sequenceFile.read())
'''
for i0 in range(9):
    for i1 in range(9):
        print(i0, ' - ', i1)
        for i2 in range(9):
            for i3 in range(9):
                for i4 in range(9):
                    for i5 in range(9):
                        for i6 in range(9):
                            for i7 in range(9):
                                for i8 in range(9):
                                    duplicate = False
                                    if i0 in [i1, i2, i3, i4, i5, i6, i7, i8]:
                                        duplicate = True
                                    if i1 in [i0, i2, i3, i4, i5, i6, i7, i8]:
                                        duplicate = True
                                    if i2 in [i0, i1, i3, i4, i5, i6, i7, i8]:
                                        duplicate = True
                                    if i3 in [i0, i1, i2, i4, i5, i6, i7, i8]:
                                        duplicate = True
                                    if i4 in [i0, i1, i2, i3, i5, i6, i7, i8]:
                                        duplicate = True
                                    if i5 in [i0, i1, i2, i3, i4, i6, i7, i8]:
                                        duplicate = True
                                    if i6 in [i0, i1, i2, i3, i4, i5, i7, i8]:
                                        duplicate = True
                                    if i7 in [i0, i1, i2, i3, i4, i5, i6, i8]:
                                        duplicate = True
                                    if i8 in [i0, i1, i2, i3, i4, i5, i6, i7]:
                                        duplicate = True
                                    if not duplicate:
                                        allSequences += [[i0, i2, i3, i4, i5, i6, i7, i8]]

sequenceFile = open('sequences.json', 'w')
sequenceFile.write(json.dumps(allSequences))
'''

def narrowSequence_Level1(i):
    coord = getMatchCoordinatesRight(cards[i[0]], cards[i[1]])
    for a in cards[i[2]]:
        for b in coord:
            if cards[i[1]][b[1]][0] == a[0] and cards[i[1]][b[1]][1] != a[1]:
                return True
    return False

def narrowSequence_Level2(i):
    coord = getMatchCoordinatesBottom(cards[i[0]], cards[i[3]])
    for a in cards[i[6]]:
        for b in coord:
            if cards[i[1]][b[1]][0] == a[0] and cards[i[1]][b[1]][1] != a[1]:
                return True
    return False

'''
fixedSequences = []
for i in allSequences:
    if narrowSequence_Level1(i):
        fixedSequences += [i]

fixedSequences2 = []
for i in fixedSequences:
    if narrowSequence_Level2(i):
        fixedSequences2 += [i]
        '''

def check4X(array):
    vals = [0,1,2,3]
    for i0 in vals:
        points0 = normalize([i0, i0+1, i0+2, i0+3])
        for i1 in vals:
            points1 = normalize([i1, i1+1, i1+2, i1+3])
            for i2 in vals:
                points2 = normalize([i2, i2+1, i2+2, i2+3])
                for i3 in vals:
                    points3 = normalize([i3, i3+1, i3+2, i3+3])
                    testArray = [
                        [
                            [array[0][points0[0]], array[0][points0[1]], array[0][points0[2]], array[0][points0[3]]],
                            [array[1][points1[0]], array[1][points1[1]], array[1][points1[2]], array[1][points1[3]]]
                        ],
                        [
                            [array[2][points2[0]], array[2][points2[1]], array[2][points2[2]], array[2][points2[3]]],
                            [array[3][points3[0]], array[3][points3[1]], array[3][points3[2]], array[3][points3[3]]]
                        ]
                    ]
                    worked = 0
                    if check(testArray, 0, 0, 1, 0):
                        worked += 1
                    elif check(testArray, 0, 0, 0, 1):
                        worked += 1
                    elif check(testArray, 0, 1, 1, 0):
                        worked += 1
                    elif check(testArray, 1, 0, 0, 1):
                        worked += 1
                    if worked == 4:
                        return True
    return False

cleaned = []
index = 0
for i in allSequences:
    if not index % 1000:
        print(index)
    if check4X(
        [
            cards[i[0]],
            cards[i[1]],
            cards[i[3]],
            cards[i[4]]
        ]
    ):
        cleaned += [i]
    index += 1

print(len(allSequences))
'''
print(len(fixedSequences))
print(len(fixedSequences2))
'''
print(len(cleaned))

for i in allSequences:
    start(i)
print("Trying card " + str(i))
start(i)