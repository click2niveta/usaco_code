def min_sprayer_applications(N, bacteria_levels):
    result = float('inf')
    total_bacteria_needed = sum(bacteria_levels)

    for L in range(1, N + 1):
        total_bacteria_added = sum(min(L, N - i) for i in range(N))
        total_bacteria_removed = sum(min(L, i + 1) for i in range(N))
        bacteria_difference = total_bacteria_added - total_bacteria_removed
        applications_needed = abs(bacteria_difference - total_bacteria_needed)
        result = min(result, applications_needed)

    return result

if __name__ == "__main__":
    N = int(input().strip())

    bacteria_levels = list(map(int, input().strip().split()))

    result = min_sprayer_applications(N, bacteria_levels)
    print(result)