N, M = map(int, input().split())
 
cows = list(map(int, input().split()))
haybales = map(int, input().split())
 
for h in haybales:
	if h <= cows[0]:
		cows[0] += h
	else:
		h_so_far = 0
		for i in range(N):
			if cows[i] > h_so_far:
				next_h = min(cows[i], h)
				cows[i] += next_h - h_so_far
				h_so_far = next_h
 
 
for c in cows:
	print(c)