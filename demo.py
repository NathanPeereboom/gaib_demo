from statistics import mean

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return fibonacci(i - 1) + fibonacci(i - 2)
    else:
        raise Exception
    
def isPalindrome(s: str):
    s = s.lower()
    s = s.strip()
    r = s[::-1]
    return s == r

def k_means_clustering(items, k):
    centroids = range(k)

    while True:
        # Reset clusters on each iteration
        clusters = []
        i = 0
        while i < k:
            clusters.append([])
            i += 1

        # Match items with nearest centroids
        for item in items:
            c = findNearest(item, centroids)
            clusters[c].append(item)
        
        # Reset centroids
        newCentroids = []
        for cluster in clusters:
            newCentroids.append(int(mean(cluster)))
        
        # Check if done
        if newCentroids == centroids:
            return clusters
        centroids = newCentroids

def findNearest(item, centroids):
    # Start by assuming the first centroid is the closest
    nearest_index = 0
    nearest_distance = abs(item - centroids[0])

    # Compare against each other centroid
    i = 1
    while i < len(centroids):
        distance = abs(item - centroids[i])
        if distance < nearest_distance:
            nearest_index = i
            nearest_distance = distance
        i += 1
    
    return nearest_index