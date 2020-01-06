test_cases = int(input())
for test_cases in range(1, test_cases+1):
    points, matches = map(int, input().split())
    if points > matches:
        winning_matches = points - matches
    if points <= matches:
        winning_matches = "0"
    print(winning_matches)
    test_cases -= 1
