distances = []
points = [(7, 9), (5, 8), (15, 4), (12, 10)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

for i in range(len(points)):
   for j in range (i+1, len(points)):
    distance = euclideanDistance(points[i], points[j])
    distances.append(distance)

    print(f"tüm mesafeler: {distances}")

    print(f"Minumum mesafe: {min(distances)}")