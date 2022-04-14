import math
def decimal_part(number: float) -> float:
  return abs(number) - abs(math.floor(number))

def normal_round(n, decimals=0):
  multiplier = 10 ** decimals
  expoN = n * multiplier
  if decimal_part(expoN) < 0.5:
    return math.floor(expoN) / multiplier
  return math.ceil(expoN) / multiplier