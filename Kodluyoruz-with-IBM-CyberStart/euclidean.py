# List containing tuples representing points in 2D space
points = [(1, 1), (4, 5), (9, 17), (15, 25)]

# Function that returns euclidean distances
def euclideanDistance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

# List of euclidean distances
distances = []

# Loop that calculates euclidean distance between each pair of points
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Print the minimum euclidean distance in the distances list
print("Minimum distance: ", min(distances))