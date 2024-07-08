import coordinateHandler as ch

def createNewMap():
  print("Creating new map...")
  print("Please enter the first coordinate")
  firstCoordinate = ch.coordinatePoint(float(input("Lat: ")), float(input("Long: ")))
  print("Please enter the second coordinate")
  secondCoordinate = ch.coordinatePoint(float(input("Lat: ")), float(input("Long: ")))
  print("Please enter the accuracy of the map")
  accuracy = int(input("Accuracy: "))
  newMap = ch.cordMap(firstCoordinate, secondCoordinate, accuracy)
  newMap.initGrid()
  newMap.printGrid()