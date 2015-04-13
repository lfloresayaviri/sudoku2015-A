# Extra Algorithm
# Sudoku solver: Chris Fallin algorithm


import string
#from make_sudoku import make_sudoku


class FallinSolver(object):
  def __init__(self):
    # initialize cells and count matrices
    self.cells = []
    self.count = []
    for i in range(9):
      self.cells += [ [] ]
      self.count += [ [] ]
      for j in range(9):
        self.cells[i] += [0]
        self.count[i] += [0]
    self.known = 0

  # makes a copy of the sudoku data
  def copy(self):
    c = FallinSolver()
    for i in range(9):
      for j in range(9):
        c.cells[i][j] = self.cells[i][j]
        c.count[i][j] = self.count[i][j]
        c.known = self.known
    return c

  # loads from external data
  def load(self, data):
    self.known = 0
    for i in range(9):
      for j in range(9):
        if(data[i][j] != 0):
          self.cells[i][j] = { data[i][j]: 1 }
          self.count[i][j] = 1
          self.known = self.known + 1
        else:
          self.cells[i][j] = {1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1}
          self.count[i][j] = 9

  # dumps to external data (ie, a simple matrix/array-of-arrays)
  def dump(self):
    out = []
    for i in range(9):
      out += [ [] ]
      for j in range(9):
        if(self.count[i][j] == 1):
          out[i] += [self.cells[i][j].keys()[0]]
        else:
          out[i] += [0]
    return out

  def load_string(self, str):
    l = str.split("\n");
    lines = []
    for line in l:
      line = line.strip()
      if(line == ''):
        continue
      row = []
      f = line.split()
      for field in f:
        field = field.strip()
        if(field == ''):
          continue
        n = string.atoi(field)
        row += [n]
      lines += [row]

    self.load(lines)

  def dump_string(self):
    out = self.dump()
    out_str = ""
    for i in range(9):
      for j in range(9):
        out_str += str(out[i][j]) + " "
        if(j % 3 == 2): out_str += "  "
      out_str += "\n"
      if(i % 3 == 2): out_str += "\n"
    return out_str

  # finds possible elements for each position
  def reduce(self):
    self.known = 0
    # for each cell:
    for i in range(9):
      for j in range(9):
        # skip this cell if it's already known
        if(self.count[i][j] == 1):
          self.known = self.known + 1
          continue
        # start with all possible
        possible = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
        # check row
        for n in range(9):
          if(self.count[i][n] == 1):
            x = self.cells[i][n].keys()[0]
            if(possible.has_key(x)):
              del possible[x]
        # check column
        for n in range(9):
          if(self.count[n][j] == 1):
            x = self.cells[n][j].keys()[0]
            if(possible.has_key(x)):
              del possible[x]
        # check inner box
        box_i = i - (i % 3)
        box_j = j - (j % 3)
        for a in range(box_i,box_i+3):
          for b in range(box_j,box_j+3):
            if(self.count[a][b] == 1):
              x = self.cells[a][b].keys()[0]
              if(possible.has_key(x)):
                del possible[x]

        # now we deal based on 'possible'
        self.count[i][j] = len(possible.keys())

        # none possible: no solutions
        if(self.count[i][j] == 0):
          return 0

        # one possible: increase number of knowns
        if(self.count[i][j] == 1):
          self.known = self.known + 1

        # store in 'cells' matrix
        self.cells[i][j] = possible

    # done: successful (ie, no impossible entries)
    return 1

  def solve(self, start = 0):

    # reduce as many times as necessary until we get no new known cells
    while 1:
      current_known = self.known
      if(self.reduce() == 0):
        return 0
      if self.known == current_known:
        break

    # all numbers known: done
    if(self.known == 9 * 9):
      return 1

    # find the first cell with more than one possibility
    x = -1
    y = -1
    flag = 0
    b = start % 9
    a = (start - b) / 9
    for i in range(a, 9):
      if(i > a): b = 0
      for j in range(b, 9):
        if(self.count[i][j] > 1):
          x = i
          y = j
          flag = 1
          break
      if flag == 1:
        break
    
    # not all numbers known, yet nothing with a possibility count > 1 ?
    # shouldn't happen
    if(x == -1 or y == -1):
      print "shouldn't happen!"
      return 0

    # try the possibilities
    possible = self.cells[x][y]
    for p in possible.keys():
      s = self.copy()
      # the recursive s.solve() call will take care of updating s.known
      s.cells[x][y] = { p: 1 }
      s.count[x][y] = 1
      if(s.solve((x * 9 + y) + 1)):
        self.cells = s.cells
        self.count = s.count
        self.known = s.known
        return 1

    # nothing worked
    return 0

default_data = """
0 6 0   1 0 4   0 5 0
0 0 8   3 0 5   6 0 0
2 0 0   0 0 0   0 0 1

8 0 0   4 0 7   0 0 6
0 0 6   0 0 0   3 0 0
7 0 0   9 0 1   0 0 4

5 0 0   0 0 0   0 0 2
0 0 7   2 0 6   9 0 0
0 4 0   5 0 8   0 7 0"""

s = FallinSolver()

print default_data + '\n'+'----------------------'

s.load_string(default_data)

if(s.solve()):
  print s.dump_string()
else:
  print "No solution could be found for the given problem. Try Again"


