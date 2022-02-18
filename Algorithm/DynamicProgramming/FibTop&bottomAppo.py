F_topdown = [-1]*50 #array to store fibonacci terms
F_bottomup = [0]*50 #array to store fibonacci terms


def dynamic_fibonacci_topdown(n):
  if (F_topdown[n] < 0):
    if (n==0):
      F_topdown[n] = 0
    elif (n == 1):
      F_topdown[n] = 1
    else:
      F_topdown[n] = dynamic_fibonacci_topdown(n-1) + dynamic_fibonacci_topdown(n-2)
  return F_topdown[n]


def fibonacci_bottom_up(n):
  F_bottomup[n] = 0
  F_bottomup[1] = 1

  for i in range(2, n+1):
    F_bottomup[i] = F_bottomup[i-1] + F_bottomup[i-2]
  return F_bottomup[n]

if __name__ == '__main__':
    print(dynamic_fibonacci_topdown(5))
    print(fibonacci_bottom_up(5))
