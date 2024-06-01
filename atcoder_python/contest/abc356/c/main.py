N, M, K = map(int, input().split())
tests = []
for i in range(M):
  value = input().split()
  keys = list(map(int, value[1:-1]))
  tests.append({'keys': keys, 'results': value[-1]})


def check_tests(test_results, correct_keys_mask, K):
    for test in test_results:
        test_mask, expected_result = test
        correct_count = bin(correct_keys_mask & test_mask).count('1')
        if (correct_count >= K and expected_result == 'x') or (correct_count < K and expected_result == 'o'):
            return False
    return True

test_results = []
for test in tests:
  mask = 0
  for key in test['keys']:
    mask |= (1 << (key - 1))
  test_results.append((mask, test['results']))
  
total_combs = 0
for correct_key_mask in range(1 << N):
  if check_tests(test_results, correct_key_mask, K):
    total_combs += 1

print(total_combs)