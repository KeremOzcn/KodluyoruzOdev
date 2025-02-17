import math

def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Örnek noktalar listesi
points = [(1, 2), (4, 6), (7, 8), (2, 1), (6, 3)]

# Tüm nokta çiftleri arasındaki mesafeyi hesaplama
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktayı tekrar tekrar kullanmamak için j=i+1 başlatıldı
        pair = (points[i], points[j])
        distance = euclideanDistance(points[i], points[j])
        distances.append((pair, distance))

# Minimum mesafeyi bulma
min_distance_pair, min_distance = min(distances, key=lambda x: x[1])

print(f"Minimum Öklid Mesafesi: {min_distance:.4f}")
print(f"Bu mesafe {min_distance_pair[0]} ve {min_distance_pair[1]} noktaları arasında.")
