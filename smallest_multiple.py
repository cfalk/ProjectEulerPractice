
def get_factors(n):
  factors = []

  d=2
  while n>1:
    while n%d==0:
      factors.append(d)
      n /= d
    d += 1

  return factors

def smallest_mult(n):
  used_factors = {}
  for i in xrange(n,1,-1):
    factors = get_factors(i)
    factor_count = {factor:factors.count(factor) for factor in factors}
    for factor, num in factor_count.iteritems():
      if not factor in used_factors:
        used_factors[factor] = num
      elif used_factors[factor]<num:
        used_factors[factor] = num

  result = 1
  for factor, num in used_factors.iteritems():
    result *= factor**num
  return result

def test():
  print "factors of 10: ",
  print get_factors(10)

  print "Smallest Multiple of numbers up to 10: ",
  print smallest_mult(10)
  print "Smallest Multiple of numbers up to 20: ",
  print smallest_mult(20)

if __name__=="__main__":
  test()
