import matplotlib.pyplot as plt
import coordinateHandler as ch
#response = requests.get("https://api.open-elevation.com/api/v1/lookup?locations=10,10|11,11|12,12|13,13|14,14|15,15|16,16|17,17")
#print(response.json())
# Plot the data 
print("This program takes in two cordinates and plots the elevation of the point on a 3D graph")
inputLat1 = float(input("Enter Latiude: "))
inputLong1 = float(input("Enter Longitude: "))
inputLat2 = float(input("Enter Latiude: "))
inputLong2 = float(input("Enter Longitude: "))
accuracy = int(input("Enter the accuracy: "))
# Create the coordinate points
point1 = ch.coordinatePoint(inputLat1, inputLong1)
point2 = ch.coordinatePoint(inputLat2, inputLong2)
grid = ch.cordMap(point1, point2, accuracy)
grid.initGrid()
grid.printGrid()