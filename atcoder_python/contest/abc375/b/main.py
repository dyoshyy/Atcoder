N = int(input())
cost_sum = 0

def calc_cost(a,b,c,d):
  return ((a-c)**2 + (b-d)**2)**0.5

x_tmp, y_tmp = 0, 0

for i in range(0, N):
  xi, yi = map(int, input().split())
  cost_sum += calc_cost(x_tmp, y_tmp, xi, yi)
  x_tmp, y_tmp = xi, yi
  
cost_sum += calc_cost(x_tmp, y_tmp, 0, 0)
  
print(cost_sum)