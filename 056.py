# return maximum digital sum till 100^100

def count(x):
  """Count the sum of all digits by digit in numer"""
    t = (int(i) for i in str(x))
    return sum(t)

m = 0 # Maximum digit sum
for a in range(100):
    for b in range(100):
        c = pow(a,b)
        C = count(c)
        if C > m :
            m = int(C)
print(m)
# 972
