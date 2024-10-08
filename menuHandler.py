import gridStorageHandler as gsh
import coordinateHandler as ch

def createNewMap(gridStorage):
  print("Creating new map...")
  mapName = input("Enter a name for your map (Leave Blank for default): ")
  if mapName == '':
    mapName = "default"
  print("Please enter the first coordinate")
  firstCoordinate = ch.coordinatePoint(float(input("Lat: ")), float(input("Long: ")))
  print("Please enter the second coordinate")
  secondCoordinate = ch.coordinatePoint(float(input("Lat: ")), float(input("Long: ")))
  print("Please enter the accuracy of the map")
  accuracy = int(input("Accuracy: "))
  newMap = ch.cordMap(firstCoordinate, secondCoordinate, accuracy, mapName)
  gridStorage.addGrid(newMap)
  mapName = gridStorage.getLastGridAdded()
  newMap.initGrid()
  #newMap.printGrid() prints without elevation data
  newMap.initElevations()
  print("Map Created! Saved as:" + mapName + " Feel free to load it")
  newMap.Visualize()

def loadMaps(gridStorage):
  print("Loading Maps...")
  gridStorage.printGrids()
  mapName = input("Enter the name of the map you want to load: ")
  gridStorage.getGrid(mapName).printGrid()

def runTests():
  print("Running tests...")
  print("Test 1 (0, 0) (0, 0) Acc 0")
  print("Generating Map...")
  testMap = ch.cordMap(ch.coordinatePoint(0, 0), ch.coordinatePoint(0, 0), 0, "test")
  print("Map created... PASSED")
  print("Initializing Grid...")
  testMap.initGrid()
  print("Grid Initialized ... PASSED")
  print("Initializing Grid Elevations...")
  testMap.initElevations()
  print("Elevations Initialized... PASSED")
  
  print("Test 2 (0, 0) (0, 0) Acc 10")
  print("Generating Map...")
  testMap = ch.cordMap(ch.coordinatePoint(0, 0), ch.coordinatePoint(0, 0), 10, "test")
  print("Map created... PASSED")
  print("Initializing Grid...")
  testMap.initGrid()
  print("Grid Initialized ... PASSED")
  print("Initializing Grid Elevations...")
  testMap.initElevations()
  print("Elevations Initialized... PASSED")
  
  print("Test 3 (-5, -5) (5, 5) Acc 3")
  print("Generating Map...")
  testMap = ch.cordMap(ch.coordinatePoint(-5, -5), ch.coordinatePoint(5, 5), 3, "test")
  print("Map created... PASSED")
  print("Initializing Grid...")
  testMap.initGrid()
  print("Grid Initialized ... PASSED")
  print("Initializing Grid Elevations...")
  testMap.initElevations()
  print("Elevations Initialized... PASSED")

  print("Test 5 (5, 5) (-5, -5) Acc 3")
  print("Generating Map...")
  testMap = ch.cordMap(ch.coordinatePoint(5, 5), ch.coordinatePoint(-5, -5), 3, "test")
  print("Map created... PASSED")
  print("Initializing Grid...")
  testMap.initGrid()
  print("Grid Initialized ... PASSED")
  print("Initializing Grid Elevations...")
  testMap.initElevations()
  print("Elevations Initialized... PASSED")

  print("Test 5 (36.33671, 115.33) (36, -115) Acc 10")
  print("Generating Map...")
  testMap = ch.cordMap(ch.coordinatePoint(36.33671, -115.33), ch.coordinatePoint(36, -115), 10, "test")
  print("Map created... PASSED")
  print("Initializing Grid...")
  testMap.initGrid()
  print("Grid Initialized ... PASSED")
  print("Initializing Grid Elevations...")
  testMap.initElevations()
  print("Elevations Initialized... PASSED")
  testMap.printGrid()

def calcDistance():
  print("Please enter 2 coordinates")
  lat1 = input("Enter Latitude 1: ")
  long1 = input("Enter Longitude 1: ")
  lat2 = input("Enter Latitude 2: ")
  long2 = input("Enter Longitude 2: ")
  firstCoordinate = ch.coordinatePoint(float(lat1), float(long1))
  secondCoordinate = ch.coordinatePoint(float(lat2), float(long2))
  result = firstCoordinate.calcDistanceTo(secondCoordinate)
  print("The distance between the two coordinates is: " + str(result))
  