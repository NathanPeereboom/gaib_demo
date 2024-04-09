def k_means_cluster(k, values):
    centroids = []
    for i in range(k):
        centroids.append(i + 1)
    while True:
        clusters = []
        for i in range(k):
            clusters.append([])
        for item in values:
            nearest_c_index = find_nearest(centroids, item)
            clusters[nearest_c_index].append(item)
        new_centroids = []
        for cluster in clusters:
            new_centroids.append(int_mean(cluster))
        if centroids == new_centroids:
            return clusters
        centroids = new_centroids

def find_nearest(centroids, item):
    nearest_distance = abs(centroids[0] - item)
    nearest_index = 0
    i = 1
    while i < len(centroids):
        distance = abs(centroids[i] - item)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_index = i
        i += 1
    return nearest_index

def int_mean(values):
    total = sum(values)
    return total // len(values)
