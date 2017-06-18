#'A' = pink
#'B' = black
#'C' = 'white'
#'D' = green
# 0 is heads
# 1 is tails
import json

# Load cards and generate side hash map
dataFile = open('penguins.json')
data = dataFile.read()
cards = json.loads(data)

sideHash = {}
for i in range(len(cards)):
    index = 0
    for a in cards[i]:
        try:
            sideHash[a[0] + str(a[1])] += [[i, index]]
        except:
            sideHash[a[0] + str(a[1])] = [[i, index]]
        index += 1

print(sideHash)

cornerstone = cards[0]

def convert(z):
    if z == -1:
        z = 3
    elif z == -2:
        z = 2
    elif z == -3:
        z = 3
    elif z == 4:
        z = 0
    elif z == 5:
        z = 1
    elif z == 6:
        z = 2
    elif z == 7:
        z = 3
    return z

def oppositeSide(key):
    if key == 1:
        return '0'
    else:
        return '1'

# Try cornerstone as the edge piece
# 1. Find the possible 2x2s
loops = 0
four = [0, 1, 2, 3]
workingFour = []
weededWorkingFour = []
for i in four:
    currentlyUsed = [0]
    sideTest0 = cornerstone[i]
    key = sideTest0[0] + oppositeSide(sideTest0[1])
    possibleCards = sideHash[key]
    for a in possibleCards:
        currentlyUsed1 = currentlyUsed
        if not a[0] in [0]:
            currentlyUsed1 += [a[0]]
            testCard1 = cards[a[0]]
            sideTest1 = testCard1[convert(a[1]-1)]
            key1 = sideTest1[0] + oppositeSide(sideTest1[1])
            possibleCards1 = sideHash[key1]
            for b in possibleCards1:
                currentlyUsed2 = currentlyUsed1
                if not b[0] in [0, a[0]]:
                    currentlyUsed2 += [b[0]]
                    testCard2 = cards[b[0]]
                    sideTest2 = testCard2[convert(b[1]-1)]
                    key2 = sideTest2[0] + oppositeSide(sideTest2[1])
                    cornerId = i+1
                    if cornerId == 4:
                        cornerId = 0
                    cornerKey = cornerstone[cornerId][0] + oppositeSide(cornerstone[cornerId][1])
                    possibleCards2 = sideHash[key2]
                    possibleCardsBottom = sideHash[cornerKey]
                    # Look at one's to the left of bottom right and bottom of top left
                    # See which cards work, cards that work are WORKING FOUR!
                    for z in possibleCards2:
                        if not z[0] in [0, a[0], b[0]]:
                            for q in possibleCardsBottom:
                                loops += 1
                                # If z[1] == 0 make q[1]+1 == 0 when right
                                if q[1] == 3:
                                    q[1] = -1
                                cornerAnd1 = i+1
                                if cornerAnd1 == 4:
                                    cornerAnd1 = 0
                                #bottomAnd2 = 
                                #if z[0] == cornerstone[cornerAnd1] == q[0] and z[1] == (q[1]+1):
                                if z[0] == q[0] and z[1] == (q[1]+1):
                                    # Glory be to god
                                    workingFour += [[
                                        [0, i],
                                        [a[0], a[1]],
                                        [b[0], b[1]],
                                        [z[0], z[1]]
                                    ]]
                                    # Now test, right, bottom, left, top
                                    # right
                                    testCardX = cards[a[0]]
                                    sideTestX = testCardX[convert(a[1]-2)]
                                    keyX = sideTestX[0] + oppositeSide(sideTestX[1])
                                    possibleCardsX = sideHash[keyX]
                                    for x in possibleCardsX:
                                        if not x[0] in [0, a[0], b[0], z[0]]:
                                            testCardY = cards[x[0]]
                                            sideTestY = testCardY[convert(x[1]-1)]
                                            keyY = sideTestY[0] + oppositeSide(sideTestY[1])
                                            possibleCardsY = sideHash[keyY]
                                            # Find other set
                                            testCardOtherY = cards[b[0]]
                                            sideTestOtherY = testCardOtherY[convert(b[1] + 1)]
                                            keyOtherY = sideTestOtherY[0] + oppositeSide(sideTestOtherY[1])
                                            possibleCardsOtherY = sideHash[keyOtherY]
                                            weeded = []
                                            for h in possibleCardsY:
                                                if not h[0] in [0, a[0], b[0], z[0], x[0]]:
                                                    for k in possibleCardsOtherY:
                                                        if h[1] == 3:
                                                            h[1] = -1
                                                        if h[0] == k[0] and k[1] == (h[1]+2):
                                                            if 3 == a[0] and 2 == b[0] and 7 == z[0]:
                                                            weededWorkingFour += [[
                                                                [0, i],
                                                                [a[0], a[1]],
                                                                [b[0], b[1]],
                                                                [z[0], z[1]]
                                                            ]]
                                                            weeded += [h]
                                            if 3 == a[0] and 2 == b[0] and 7 == z[0]:
                                                doNothing = True
                                            if len(weeded) > 0:
                                                print('Weeded!')
                                            if len(weeded) > 0:
                                                weededWorkingFour += [[
                                                    [0, i],
                                                    [a[0], a[1]],
                                                    [b[0], b[1]],
                                                    [z[0], z[1]]
                                                ]]

for i in weededWorkingFour:
    print(i)

print(len(weededWorkingFour))
print(len(workingFour))

print(loops)
