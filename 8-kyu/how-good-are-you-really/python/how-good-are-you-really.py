def better_than_average(class_points, your_points):
    class_points.append(your_points)
    return sum(class_points) / len(class_points) < your_points