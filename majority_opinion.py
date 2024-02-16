# def focus_groups(preferences):
#     result = []

#     for pref in preferences:
#         hay_counts = {}
#         max_count = 0
#         candidate_hay = -1

#         for i, h in enumerate(pref, start=1):
#             if h not in hay_counts:
#                 hay_counts[h] = 0
#             hay_counts[h] += 1

#             if hay_counts[h] > max_count:
#                 max_count = hay_counts[h]
#                 candidate_hay = h

#             if max_count > i / 2:
#                 result.append(candidate_hay)
#                 break
#         else:
#             result.append(-1)

#     return result

# num_tests = int(input())
# test_cases = []

# for _ in range(num_tests):
#     n = int(input())
#     preferences = list(map(int, input().split()))
#     #print(preferences)
#     test_cases.append(preferences)

# output = focus_groups(test_cases)
# for o in output:
#     if isinstance(o, int):
#         print(o)
#     else:
#         print(" ".join(map(str, sorted(o))))



# def find_preferred_hay(N, preferences):
#     def majority_element(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         candidate = None
#         count = 0

#         for num in arr:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1

#         return candidate

#     def is_majority(preferred_hay, arr):
#         # Check if the preferred hay is the majority in the array
#         count = arr.count(preferred_hay)
#         return count > len(arr) // 2

#     def find_preferred_hay_recursive(left, right):
#         if left == right:
#             # Base case: Single cow, return her preferred hay
#             return preferences[left]

#         mid = (left + right) // 2

#         # Divide the problem into two halves
#         left_majority = find_preferred_hay_recursive(left, mid)
#         right_majority = find_preferred_hay_recursive(mid + 1, right)

#         # Check if either of the halves has a majority element
#         if is_majority(left_majority, preferences[left:right + 1]):
#             return left_majority
#         elif is_majority(right_majority, preferences[left:right + 1]):
#             return right_majority

#         # If no majority in either half, check the whole array
#         return majority_element(preferences[left:right + 1])

#     preferred_hay = find_preferred_hay_recursive(0, N - 1)

#     # Check if the preferred hay is a majority in the entire array
#     if is_majority(preferred_hay, preferences):
#         result = sorted([preferred_hay] * preferences.count(preferred_hay))
#     else:
#         result = [-1]  # No hay type is liked by all cows

#     return set(result)

# # Read the number of test cases
# T = int(input())

# # Store results for each test case
# all_results = []

# # Process each test case
# for _ in range(T):
#     N = int(input())
#     preferences = list(map(int, input().split()))

#     result = find_preferred_hay(N, preferences)
#     all_results.append(result)

# # Print the results after all test cases
# for result in all_results:
#     print(*result)


# from collections import Counter

# def find_preferred_hay(N, preferences):
#     def majority_element(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         candidate = None
#         count = 0

#         for num in arr:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1

#         return candidate

#     counter = Counter(preferences)
#     majority_hay = majority_element(preferences)

#     # Check if the majority hay is liked by more than half the cows
#     if counter[majority_hay] > N // 2:
#         result = [majority_hay]
#     else:
#         result = [-1]  # No hay type is liked by all cows

#     return result

# # Read the number of test cases
# T = int(input())

# # Store results for each test case
# all_results = []

# # Process each test case
# for _ in range(T):
#     N = int(input())
#     preferences = list(map(int, input().split()))

#     result = find_preferred_hay(N, preferences)
#     all_results.append(result)

# # Print the results after all test cases
# for result in all_results:
#     print(*result)



# def find_preferred_hay(N, preferences):
#     def majority_element(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         candidate = None
#         count = 0

#         for num in arr:
#             if count == 0:
#                 candidate = num
#             count += 1 if num == candidate else -1

#         return candidate

#     majority_hay = majority_element(preferences)

#     # Check if the majority hay is liked by more than half the cows
#     if preferences.count(majority_hay) > N // 2:
#         print(majority_hay)
#     else:
#         print(-1)  # No hay type is liked by all cows


# # Read the number of test cases
# T = int(input())

# # Process each test case
# for _ in range(T):
#     N = int(input())
#     preferences = list(map(int, input().split()))

#     find_preferred_hay(N, preferences)



# def find_preferred_hay(N, preferences):
#     def majority_element(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         candidate1, candidate2 = None, None
#         count1, count2 = 0, 0

#         for num in arr:
#             if count1 == 0:
#                 candidate1 = num
#             elif count2 == 0:
#                 candidate2 = num

#             count1 += 1 if num == candidate1 else -1
#             count2 += 1 if num == candidate2 else -1

#         return candidate1, candidate2

#     majority_hay1, majority_hay2 = majority_element(preferences)

#     # Check if the majority hays are liked by more than half the cows
#     count1 = preferences.count(majority_hay1)
#     count2 = preferences.count(majority_hay2)

#     if count1 > N // 2 and count2 > N // 2:
#         print(majority_hay1, majority_hay2)
#     elif count1 > N // 2:
#         print(majority_hay1)
#     elif count2 > N // 2:
#         print(majority_hay2)
#     else:
#         print(-1)  # No hay type is liked by all cows

# # Read the number of test cases
# T = int(input())

# # Process each test case
# for _ in range(T):
#     N = int(input())
#     preferences = list(map(int, input().split()))

#     find_preferred_hay(N, preferences)



# def find_preferred_hay(N, preferences):
#     def majority_elements(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         candidate1, candidate2 = None, None
#         count1, count2 = 0, 0

#         for num in arr:
#             if num == candidate1:
#                 count1 += 1
#             elif num == candidate2:
#                 count2 += 1
#             elif count1 == 0:
#                 candidate1 = num
#                 count1 = 1
#             elif count2 == 0:
#                 candidate2 = num
#                 count2 = 1
#             else:
#                 count1 -= 1
#                 count2 -= 1

#         return candidate1, candidate2

#     majority_hay1, majority_hay2 = majority_elements(preferences)

#     # Check if the majority hays are liked by more than one-third of the cows
#     count1 = preferences.count(majority_hay1)
#     count2 = preferences.count(majority_hay2)

#     results = []
#     if count1 > N // 3 and count2 > N // 3:
#         results.append((majority_hay1, majority_hay2))
#     elif count1 > N // 3:
#         results.append((majority_hay1,))
#     elif count2 > N // 3:
#         results.append((majority_hay2,))
#     else:
#         results.append((-1,))  # No hay type is liked by all cows

#     return results

# # Read the number of test cases
# T = int(input())

# # Store all results for each test case
# all_results = []

# # Process each test case
# for _ in range(T):
#     N = int(input())
#     preferences = list(map(int, input().split()))

#     results = find_preferred_hay(N, preferences)
#     all_results.extend(results)

# # Print all results at once
# for result in all_results:
#     print(*result)



# def find_hay(N, p):
#     def elements_maj(arr):
#         # Boyer-Moore Majority Vote Algorithm
#         c1, c2 = None, None
#         count1, count2 = 0, 0

#         for num in arr:
#             if num == c1:
#                 count1 += 1
#             elif num == c2:
#                 count2 += 1
#             elif count1 == 0:
#                 c1 = num
#                 count1 = 1
#             elif count2 == 0:
#                 c2 = num
#                 count2 = 1
#             else:
#                 count1 -= 1
#                 count2 -= 1

#         return c1, c2

#     majority_hay1, majority_hay2 = elements_maj(p)

#     # Check if the majority hays are liked by more than half the cows
#     count1 = p.count(majority_hay1)
#     count2 = p.count(majority_hay2)
#     #preference_dist_cnt = len(set(preferences))
#     # print(f"count1: {count1} count2: {count2}")
#     # print(f" N // 2: { N // 2}")


#     if N == 2 and len(set(p)) == 2:
#          print(-1) 
#     elif count1 > (N // 3) and count2 > (N // 3):
#         print(majority_hay1, majority_hay2)
#     elif count1 > (N // 3):
#         print(majority_hay1)
#     elif count2 > (N // 3):
#         print(majority_hay2)
#     else:
#         print(-1)  # No hay type is liked by all cows

# # Read the number of test cases
# TC = int(input())

# # Process each test case
# for _ in range(TC):
#     N = int(input())
#     p = list(map(int, input().split()))

#     find_hay(N, p)