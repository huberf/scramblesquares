# Scramble Squares Auto Solver

Scramble squares is a deceptively simple game of nine pieces you must arrange in
the proper order and orientation for all edges to match the adjacent edges.
Despite this seemingly simple setup, there are 95,126,814,720 (95 billion)
possible permutations. A simply random approach to a solution using ones hands
would take a lifetime. However, there are computational ways to shrink the total
time down to the blink of an eye on a standard computer.

If you like the notion of completing a challenge like this, don't read further
or look at these problems as it will obviously spoil the joy brought from
generating the solution on your own. For others, these scripts contain the
complete method for solving the puzzle.

## Setup
* First you must clone this repo via `git clone
  https://github.com/huberf/scramblesquares`
* Then, you must input your cards into a .json file. Scramble Squares has four
  unique image kinds and a top and bottom of each. Select any character sequence
  to represent the different types and then choose to represent heads with a 1
  and tails with a 0 or vice versa. The important thing here is that you are
  consistent. It doesn't matter what you choose so long as you don't
  accidentilly name something incorrectly. I recommend you also number cards in
  the order you wrote them in the .json file, and it will help a LOT if you also
  mark what the "top" of the card is. This is the first side you input for that
  card.
* Now, run `python3 solve.py` and it will spit out the solution set you need to
  try. (Note: currently, it spits out a short list of the possible core
  configurations, so as of right now you will need to do a little bit of testing
  yourself, but this should be very short.

## Theory
As noted above and inherently obvious, this will contain spoilers for the solution.
The goal of any algorithm should be to identify the solution in as few
processing cycles as possible. Every possible configuration will always have a
randomly selected card (called the cornerstone from here on out) in one of four
orientations. This card will always form a square with at least three other
cards. If it is at a corner, there will only be one such 2 by 2 square it forms,
but if it is in the middle of an edge, there will be 2 such squares, and if it
is in the center there will be 4 of these squares. Therefore, if one randomly
selects a card to be the cornerstone, and find all possible 2 by 2 squares the
otehr cards can form with it, this set of values will contain the actual
solution itself. If one iterates through the four possible rotations of the
cornerstone, and see what squares can be formed with it at the upper left of the
2 by 2, you can cut down the number of computations from 95 billion to 1,344
which is a very quick thing to process.
The way this reduction happens, is the program initially loads the cards and
caches them in a hashmap with the keys representing the type of each side. For
instance D0 might represent the head of a Donkey symbol and D1 would inversely
represent the lower section of a Donkey symbol.
When identifying possible working 2 by 2s, one can find the possible cards that
could hook up to the edge of the cornerstone currently to its right. If this
edge is represented by D0, one must only query the hashmap for all cards with
the edge D1.
One then tests these cards in a simple loop, and following the above logic
places a card below that card (the bottom right location). Then, the system
automatically identifies which cards can possibly fit below the cornerstone and
to the left of the third card. The cards that work here are possible solutions.
One then rotates the cornerstone clockwise and repeats, saving the possible
solutions at each step.

To narrow one then must run a couple of quick checks, which I will elaborate
more on a future README update.

## To-Do
Make algorithm return only the completely working solution.
