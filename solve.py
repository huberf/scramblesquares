# Example card type key
#'A' = pink
#'B' = black
#'C' = 'white'
#'D' = green
# 0 is heads
# 1 is tails
import json

# Load cards and generate side hash map
print('Enter the name of the JSON file holding your card data.')
fileName = input('> ')
dataFile = open(fileName)
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

# Uncomment if cards don't seem to be being identified properly
# print(sideHash)

# Select the first card to be the main card to test off of
cornerstone = cards[0]

# Convert a side value between -3 and 7 to the normalized 0-3 scale
# Side 0 is the first side input in your card data file and 3 is the last one
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

# Return the corresponding value for complementary piece for the card graphic
# E.G. for a heads piece, return the value for a tails piece.
def oppositeSide(key):
    if key == 1:
        return '0'
    else:
        return '1'

# This algorithm will be used later on after identifying the possible 2 by 2s
# You don't need to understand or use it yet
def crackSideFit(cards, a, b, aOffset, bOffset, xOffset, finalOffset, searchHit):
    testCardX = cards[a[0]]
    sideTestX = testCardX[convert(a[1]-aOffset)]
    keyX = sideTestX[0] + oppositeSide(sideTestX[1])
    possibleCardsX = sideHash[keyX]
    weeded = []
    for x in possibleCardsX:
        if not x[0] in searchHit:
            testCardY = cards[x[0]]
            sideTestY = testCardY[convert(x[1]-1)]
            keyY = sideTestY[0] + oppositeSide(sideTestY[1])
            possibleCardsY = sideHash[keyY]
            # Find other set
            testCardOtherY = cards[b[0]]
            sideTestOtherY = testCardOtherY[convert(b[1] + bOffset)]
            keyOtherY = sideTestOtherY[0] + oppositeSide(sideTestOtherY[1])
            possibleCardsOtherY = sideHash[keyOtherY]
            for h in possibleCardsY:
                tempSearch = searchHit + [x[0]]
                if not h[0] in tempSearch:
                    for k in possibleCardsOtherY:
                        if h[1] == 3:
                            h[1] = -1
                        if h[0] == k[0] and k[1] == (h[1]+xOffset):
                            weeded += [h]
            if 3 == a[0] and 2 == b[0] and 7 == z[0]:
                doNothing = True
    if len(weeded) > 0:
        return True
    else:
        return False

#####################################
# Try cornerstone as the edge piece #
# 1. Find the possible 2x2s         #
#####################################
# Simple variable for determine speed and depth of algorithm
loops = 0
# The four possible sides for use in rotating the cornerstone
four = [0, 1, 2, 3]
# Variable to store possible working 2 by 2 sets
workingFour = []
# Secondary variable for values that have been further vetted
weededWorkingFour = []
# Loop through the possible orientations of the cornerstone
for i in four:
    # Load the data for the side one is testing
    sideTest0 = cornerstone[i]
    # Construct the key to be used with the hash map to find the side complement
    key = sideTest0[0] + oppositeSide(sideTest0[1])
    # Load all the cards that have a side matching the key (this will also include the edge that has that value)
    possibleCards = sideHash[key]
    # Loop through the possible cards, testing how they work
    for a in possibleCards:
        # Make sure that the card you are testing adding to the cornerstone is in fact not the cornerstone
        if not a[0] in [0]:
            # Load the card a represents via its index
            testCard1 = cards[a[0]]
            # Determine the side which is one to the clockwise from the edge touching the cornerstone
            sideTest1 = testCard1[convert(a[1]-1)]
            # Determine the key for the complement of that bottom side
            key1 = sideTest1[0] + oppositeSide(sideTest1[1])
            # Determine possible cards
            possibleCards1 = sideHash[key1]
            # Loop through this second level of possible cards
            for b in possibleCards1:
                # Ensure that the card in testing isn't the cornerstone or the card a being tested
                if not b[0] in [0, a[0]]:
                    # Load the card being tested
                    testCard2 = cards[b[0]]
                    # Load the side being tested (one counterclockwise)
                    sideTest2 = testCard2[convert(b[1]-1)]
                    # Generate the key to test possible connections
                    key2 = sideTest2[0] + oppositeSide(sideTest2[1])
                    # Determine the appropriate side for testing against the cornerstone
                    # This is one clockwise
                    # Remember: we are trying to determine which cards fit between the cornerstone and card b
                    # hence the work we are doing here
                    cornerId = i+1
                    if cornerId == 4:
                        cornerId = 0
                    # Determine the key for the bottom cornerstone complement
                    cornerKey = cornerstone[cornerId][0] + oppositeSide(cornerstone[cornerId][1])
                    # Determine possible cards against card b
                    possibleCards2 = sideHash[key2]
                    # Determine the possible cards against the bottom of the cornerstone
                    possibleCardsBottom = sideHash[cornerKey]
                    # Look at one's to the left of bottom right and bottom of top left
                    # See which cards work, cards that work are WORKING FOUR!
                    for z in possibleCards2:
                        # Ensure the card in testing is not already in use
                        if not z[0] in [0, a[0], b[0]]:
                            for q in possibleCardsBottom:
                                loops += 1
                                # If z[1] == 0 make q[1]+1 == 0 when right
                                if q[1] == 3:
                                    q[1] = -1
                                cornerAnd1 = i+1
                                if cornerAnd1 == 4:
                                    cornerAnd1 = 0
                                # If the card z and q are the same card and the sides that fit against the cornerstone and b are directly beside eachother
                                # in the right direction, then this is a working 2 by 2
                                if z[0] == q[0] and z[1] == (q[1]+1):
                                    # Identified working 2 by 2 and add to the proper var
                                    workingFour += [[
                                        [0, i],
                                        [a[0], a[1]],
                                        [b[0], b[1]],
                                        [z[0], z[1]]
                                    ]]
                                    # Now test, right, bottom, left, top
                                    # Var for total working sides
                                    totalWorkit = 0
                                    # Right
                                    if crackSideFit(cards, a, b, -2, 1, -1, 2, [0, a[0], b[0], z[0]]):
                                        totalWorkit += 1
                                    # Top
                                    if crackSideFit(cards, [0, i], a, -1, 1, -1, 1, [0, a[0], b[0], z[0]]):
                                        totalWorkit += 1
                                    # Left
                                    if crackSideFit(cards, z, [0, i], -2, -2, -1, 1, [0, a[0], b[0], z[0]]):
                                        totalWorkit += 1
                                    # Bottom
                                    if crackSideFit(cards, b, z, -2, 1, -1, 1, [0, a[0], b[0], z[0]]):
                                        totalWorkit += 1
                                    if totalWorkit > 1:
                                        # Further vetting done and passed so adding to proper var
                                        weededWorkingFour += [[
                                            [0, i],
                                            [a[0], a[1]],
                                            [b[0], b[1]],
                                            [z[0], z[1]]
                                        ]]
                                        # Uncomment if weeding doesn't seem to be working and add additional print statements as needed
                                        # print('Weeding one!')

# Print out results
for i in weededWorkingFour:
    print(i)

# Determine how well the weeding algorithm worked
print(len(weededWorkingFour))
print(len(workingFour))

# Print the efficiency of the algorithm
print(loops)
