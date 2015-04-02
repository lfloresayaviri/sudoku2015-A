# make_sudoku.py

#import sys, os, random, getopt, re

import random

def main():

  puzzles = [makepuzzle(solution([None] * 81))]
  for puzzle in puzzles:
    print printboard(puzzle)

def makepuzzle(board):
  puzzle = []; deduced = [None] * 81
  order = random.sample(xrange(81), 81)
  for pos in order:
    if deduced[pos] is None:
      puzzle.append((pos, board[pos]))
      deduced[pos] = board[pos]
      deduce(deduced)
  return boardforentries(puzzle)

def boardforentries(entries):
  board = [None] * 81
  for pos, n in entries: board[pos] = n
  return board

def solution(board):
	return solveboard(board)[1]

def solveboard(original):
  board = list(original)
  guesses = deduce(board)
  if guesses is None: return ([], board)
  track = [(guesses, 0, board)]
  return solvenext(track)

def solvenext(remembered):
  while len(remembered) > 0:
    guesses, c, board = remembered.pop()
    if c >= len(guesses): continue
    remembered.append((guesses, c + 1, board))
    workspace = list(board)
    pos, n = guesses[c]
    workspace[pos] = n
    guesses = deduce(workspace)
    if guesses is None: return (remembered, workspace)
    remembered.append((guesses, 0, workspace))
  return ([], None)

def printcode(n):
  if n is None: return '*'
  return str(n + 1)

def printboard(board):
  out = '-----------------------\n'
  y = 8
  for matrix in xrange(81):
  	out += printcode(board[matrix]) + ' '
  	if ((matrix % 3) == 2):
  		out += "| "
  	if (matrix == y):
  		out += '\n'
  		if ((matrix >= 19) and (matrix <= 27)) or ((matrix >= 45) and (matrix <= 54)):
  			out += '-----------------------\n'
  		y += 9
  out += '-----------------------\n'
  return out


# def boardmatches(b1, b2):
#   for i in xrange(81):
#     if b1[i] != b2[i]: return False
#   return True

def deduce(board):
  while True:
    stuck, guess, count = True, None, 0
    # fill in any spots determined by direct conflicts
    allowed, needed = figurebits(board)
    for pos in xrange(81):
      if None == board[pos]:
        numbers = listbits(allowed[pos])
        if len(numbers) == 0: return []
        elif len(numbers) == 1: board[pos] = numbers[0]; stuck = False
        elif stuck:
          guess, count = pickbetter(guess, count, [(pos, n) for n in numbers])
    if not stuck: allowed, needed = figurebits(board)
    # fill in any spots determined by elimination of other locations
    for axis in xrange(3):
      for x in xrange(9):
        numbers = listbits(needed[axis * 9 + x])
        for n in numbers:
          bit = 1 << n
          spots = []
          for y in xrange(9):
            pos = posfor(x, y, axis)
            if allowed[pos] & bit: spots.append(pos)
          if len(spots) == 0: return []
          elif len(spots) == 1: board[spots[0]] = n; stuck = False
          elif stuck:
            guess, count = pickbetter(guess, count, [(pos, n) for pos in spots])
    if stuck:
      if guess is not None: random.shuffle(guess)
      return guess

def figurebits(board):
  allowed, needed = [e is None and 511 or 0 for e in board], []
  for axis in xrange(3):
    for x in xrange(9):
      bits = axismissing(board, x, axis)
      needed.append(bits)
      for y in xrange(9):
        allowed[posfor(x, y, axis)] &= bits
  return allowed, needed

def axismissing(board, x, axis):
  bits = 0
  for y in xrange(9):
    e = board[posfor(x, y, axis)]
    if e is not None: bits |= 1 << e
  return 511 ^ bits

def posfor(x, y, axis = 0):
  if axis == 0: return x * 9 + y
  elif axis == 1: return y * 9 + x
  else: return ((0,3,6,27,30,33,54,57,60)[x] + (0,1,2,9,10,11,18,19,20)[y])

def listbits(bits):
  return [y for y in xrange(9) if 0 != bits & 1 << y]

def pickbetter(b, c, t):
  if b is None or len(t) < len(b): return (t, 1)
  if len(t) > len(b): return (b, c)
  if random.randint(0, c) == 0: return (t, c + 1)
  else: return (b, c + 1)

main()