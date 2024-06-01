N, M = map(int, input().split())

MOD = 998244353

def count_ones_in_range(n, bit):
    block_size = 1 << (bit + 1)
    full_blocks = (n + 1) // block_size
    remainder = (n + 1) % block_size
    return full_blocks * (1 << bit) + max(0, remainder - (1 << bit))

total = 0
bit = 0

while (1 << bit) <= M or (1 << bit) <= N:
  if M & (1 << bit):
    total += count_ones_in_range(N, bit)
    total %= MOD
  
  bit += 1

print(total)
