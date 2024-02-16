def broken_targets(N, S, locations, p=1, d=1):
    current_loc = S
    visited_list = [False] * (N + 1)
    broken_targets_set = set()

    while 1 <= current_loc <= N:
        if locations[current_loc - 1][0] == 1:
            if not visited_list[current_loc]:
                if p >= locations[current_loc - 1][1]:
                    broken_targets_set.add(current_loc)
                    visited_list[current_loc] = True
        else:
            p += locations[current_loc - 1][1]
            d *= -1
        current_loc += d * p

    return len(broken_targets_set)

n, s = map(int, input().split())
locations = [tuple(map(int, input().split())) for _ in range(n)]

print(broken_targets(n, s, locations))