from re import error
import coordinateHandler as ch

class gridStorage:
  def __init__(self):
    self.grids = {}
    self.lastGridAdded = str()
  def printGrids(self):
    for grid in self.grids.values():
      print(grid.getName())
  def findNextName(self, name):
    copies = 2
    while self.grids.get(name + str(copies)) is not None:
      copies += 1
    return name + str(copies)
  def addGrid(self, grid):
    if self.grids.get(grid.getName()) is not None:
      nameToStoreUnder = self.findNextName(grid.getName())
      self.grids[nameToStoreUnder] = grid
      self.lastGridAdded = nameToStoreUnder
    else:
      nameToStoreUnder = grid.getName()
      self.grids[nameToStoreUnder] = grid
      self.lastGridAdded = nameToStoreUnder
  def removeGrid(self, gridName):
    self.grids.pop(gridName)
  def getGrid(self, gridName):
    if self.grids.get(gridName) is None:
      raise error("Grid does not exist")
    else:
      return self.grids[gridName]
  def getLastGridAdded(self):
    return self.lastGridAdded