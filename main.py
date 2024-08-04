import matplotlib.pyplot as plt
import menuHandler as mh
import gridStorageHandler as gsh
#response = requests.get("https://api.open-elevation.com/api/v1/lookup?locations=10,10|11,11|12,12|13,13|14,14|15,15|16,16|17,17")
#print(response.json())
# Plot the data 
programRunning = True
gridStorage = gsh.gridStorage()
print("This program takes in two cordinates and plots the elevation of the point on a 3D graph")
while programRunning:
  print("1: Create New Map")
  print("2: Load Map")
  print("3 DEBUG")
  print("4 Calculate Distances W/ Coordinates")
  print("Q: Quit")
  choice = input("Enter your choice: ")
  match choice:
    case "1":
      mh.createNewMap(gridStorage)
    case "2":
      mh.loadMaps(gridStorage)
    case "3":
      mh.runTests()
    case "4":
      mh.calcDistance()
    case "Q":
      print("Closing Program...")
      programRunning = False
      break