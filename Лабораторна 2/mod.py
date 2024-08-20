def calculate_distance(n):
    current_distance = 10
    total_distance = 0

    for day in range(n):
        total_distance += current_distance
        current_distance *= 1.1

    return total_distance
